import os
import shutil
import zipfile
import hashlib
import json
import re
from pypdf import PdfReader

root_dir = "/Users/norbertodimarco/Downloads/Antigravity/prepsecplus"
log_md_path = os.path.join(root_dir, "process_log.md")
pdfs_json_path = os.path.join(root_dir, "pdfs.json")

# Folders to ignore
ignored_dirs = {".git", "node_modules"}

log_moved = []
log_zips = []
log_pdfs = []
log_duplicates = []
log_deleted_dirs = []

def get_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"error_{e}"

def get_unique_filename(dest_dir, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_dir, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

# 1. Unzip archives directly to the root, flattening their structure
def extract_and_flatten_zips():
    # Find all zips in root
    zips = [f for f in os.listdir(root_dir) if f.lower().endswith(".zip")]
    
    for zip_name in zips:
        zip_path = os.path.join(root_dir, zip_name)
        log_zips.append(zip_name)
        print(f"Extracting and flattening ZIP: {zip_name}...")
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for member in zip_ref.infolist():
                    if member.is_dir():
                        continue
                    # Get only the base filename (flattening)
                    filename = os.path.basename(member.filename)
                    if not filename or filename == ".DS_Store":
                        continue
                        
                    # Extract file content directly to root with unique name
                    dest_filename = get_unique_filename(root_dir, filename)
                    dest_path = os.path.join(root_dir, dest_filename)
                    
                    # Extract raw data and write it
                    with zip_ref.open(member) as source_file:
                        with open(dest_path, "wb") as target_file:
                            shutil.copyfileobj(source_file, target_file)
                            
                    log_moved.append(f"Extracted from {zip_name}: '{member.filename}' -> '{dest_filename}'")
        except Exception as e:
            print(f"Failed to extract {zip_name}: {e}")
            log_moved.append(f"FAILED to extract {zip_name}: {e}")

# 2. PDF to Markdown conversion using pypdf
def convert_pdf_to_md(pdf_path, md_path):
    print(f"Converting PDF to Markdown: {os.path.basename(pdf_path)}...")
    try:
        reader = PdfReader(pdf_path)
        markdown_lines = []
        
        # Add a title header
        title_base = os.path.splitext(os.path.basename(pdf_path))[0]
        markdown_lines.append(f"# {title_base}\n")
        
        for page_idx, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue
                
            markdown_lines.append(f"## Page {page_idx + 1}\n")
            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Basic Markdown parsing heuristics:
                # - If the line is short, capitalized, and doesn't end in punctuation, it might be a subheader
                if len(line) < 60 and line.isupper() and not line.endswith(('.', ',', ';', ':', '!', '?')):
                    markdown_lines.append(f"### {line.title()}\n")
                # - If the line starts with a bullet point indicator
                elif line.startswith(('-', '*', '•', 'o', '+')):
                    # Normalize list bullet
                    clean_line = line.lstrip('-*•o+ ').strip()
                    markdown_lines.append(f"- {clean_line}")
                # - If it's a numbered list line
                elif re.match(r"^\d+[\.\)]", line):
                    markdown_lines.append(line)
                else:
                    markdown_lines.append(line + "\n")
                    
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("\n".join(markdown_lines))
        return True
    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        return False

def process_pdfs():
    # Find all PDFs in root folder
    pdfs = [f for f in os.listdir(root_dir) if f.lower().endswith(".pdf")]
    
    pdf_manifest = []
    for pdf_name in pdfs:
        pdf_path = os.path.join(root_dir, pdf_name)
        md_name = os.path.splitext(pdf_name)[0] + ".md"
        md_path = os.path.join(root_dir, md_name)
        
        success = convert_pdf_to_md(pdf_path, md_path)
        if success:
            log_pdfs.append(f"Converted '{pdf_name}' to '{md_name}'")
            pdf_manifest.append({
                "title": os.path.splitext(pdf_name)[0].replace("_", " ").title(),
                "pdf_path": f"./{pdf_name}",
                "md_path": f"./{md_name}"
            })
        else:
            log_pdfs.append(f"FAILED to convert '{pdf_name}'")
            
    # Save PDF manifest for the web portal
    with open(pdfs_json_path, "w", encoding="utf-8") as f:
        json.dump(pdf_manifest, f, indent=2, ensure_ascii=False)
    print(f"PDF manifest written to {pdfs_json_path}")

# 3. Detect duplicate files by name and MD5 content hash
def detect_duplicates():
    files_by_name = {}
    files_by_hash = {}
    
    # Scan files in root directory
    for f in os.listdir(root_dir):
        file_path = os.path.join(root_dir, f)
        if os.path.isdir(file_path) or f.startswith(".") or f == "process_log.md" or f == "flatten_log.txt":
            continue
            
        # 1. Check duplicate names (since we rename them to base_1.ext, we can group by original name)
        # Let's extract original name if it has _\d+ suffix
        m = re.match(r"^(.*?)(?:_\d+)?(\.[^.]+)$", f)
        if m:
            orig_name = m.group(1) + m.group(2)
            files_by_name.setdefault(orig_name, []).append(f)
            
        # 2. Check duplicate contents via MD5 hash
        file_hash = get_md5(file_path)
        if not file_hash.startswith("error_"):
            files_by_hash.setdefault(file_hash, []).append(f)
            
    # Format duplicate name report
    log_duplicates.append("### Duplicates by Name (Original Name Groups)")
    has_name_dups = False
    for orig, matches in files_by_name.items():
        if len(matches) > 1:
            has_name_dups = True
            log_duplicates.append(f"- **{orig}**: {', '.join(matches)}")
    if not has_name_dups:
        log_duplicates.append("- None found.")
        
    # Format duplicate content report
    log_duplicates.append("\n### Duplicates by Content (MD5 Hash Groups)")
    has_hash_dups = False
    for fhash, matches in files_by_hash.items():
        if len(matches) > 1:
            has_hash_dups = True
            log_duplicates.append(f"- **Hash {fhash[:8]}...**: {', '.join(matches)}")
    if not has_hash_dups:
        log_duplicates.append("- None found.")

# 4. Clean up empty subdirectories
def clean_empty_directories():
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs]
        
        if os.path.abspath(dirpath) == os.path.abspath(root_dir):
            continue
            
        # Ignore if it's inside .git or node_modules
        rel_path = os.path.relpath(dirpath, root_dir)
        path_parts = rel_path.split(os.sep)
        if any(part in ignored_dirs for part in path_parts):
            continue
            
        # Delete DS_Store
        ds_store = os.path.join(dirpath, ".DS_Store")
        if os.path.exists(ds_store):
            try:
                os.remove(ds_store)
            except:
                pass
                
        # Check empty
        try:
            if not os.listdir(dirpath):
                os.rmdir(dirpath)
                log_deleted_dirs.append(dirpath)
                print(f"Deleted folder: {dirpath}")
        except Exception as e:
            print(f"Failed to delete empty folder {dirpath}: {e}")

# 5. Write Markdown Process Log
def write_process_log():
    log_content = [
        "# Workspace Asset Processing Log\n",
        "This log documents all file movements, ZIP extractions, PDF to Markdown conversions, and duplicates detected during the process.\n",
        "## 1. ZIP Archives Extracted",
        "\n".join([f"- {z}" for z in log_zips]) if log_zips else "- None found.",
        "\n## 2. Files Extracted / Moved to Root",
        "\n".join([f"- {m}" for m in log_moved]) if log_moved else "- None moved.",
        "\n## 3. PDFs Converted to Markdown",
        "\n".join([f"- {p}" for p in log_pdfs]) if log_pdfs else "- None converted.",
        "\n## 4. Duplicate Files Detected (Awaiting Review)",
        "\n".join(log_duplicates),
        "\n## 5. Empty Folders Deleted",
        "\n".join([f"- {d}" for d in log_deleted_dirs]) if log_deleted_dirs else "- None deleted."
    ]
    
    with open(log_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_content))
    print(f"Log written to {log_md_path}")

def run_pipeline():
    # Step 1: Extract and flatten ZIP files
    extract_and_flatten_zips()
    
    # Step 2: Convert PDFs to Markdown and generate pdfs.json manifest
    process_pdfs()
    
    # Step 3: Detect duplicates
    detect_duplicates()
    
    # Step 4: Clean up empty subfolders
    clean_empty_directories()
    
    # Step 5: Write the markdown process log
    write_process_log()

if __name__ == "__main__":
    run_pipeline()
