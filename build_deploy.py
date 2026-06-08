#!/usr/bin/env python3
"""
build_deploy.py
Builds the Vite project and structures it for Ferozo deployment.
Uses hardlinks for fast copying of heavy media files if on the same volume.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
OUTPUT = os.path.join(ROOT, "public_html", "splus")

# List of JSON files required by the portal
JSON_FILES = [
    "study_days.json",
    "domains.json",
    "exam_objectives.json",
    "questions.json",
    "flashcards.json",
    "videos.json",
    "schedule.json",
    "pdfs.json"
]

# List of server/SEO configuration files
CONFIG_FILES = [
    ".htaccess",
    "contact.php",
    "robots.txt",
    "sitemap.xml",
    "favicon.ico"
]

def run_cmd(cmd, cwd=ROOT):
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, shell=False)
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(cmd)}")
        sys.exit(result.returncode)

def safe_copy(src, dest):
    """Try to hardlink first for speed/space, fallback to copying if different volumes."""
    if os.path.exists(dest):
        os.remove(dest)
    try:
        os.link(src, dest)
    except OSError:
        shutil.copy2(src, dest)

def main():
    print("==========================================")
    # 1. Run Vite Build
    print("Building Vite frontend with relative base paths...")
    run_cmd(["npx", "vite", "build", "--base", "./"])
    
    if not os.path.exists(DIST):
        print("Error: dist/ directory was not created by the build process.")
        sys.exit(1)
        
    # 2. Prepare Output Directory
    print(f"\nPreparing output directory: {OUTPUT}")
    if os.path.exists(OUTPUT):
        print(f"Clearing old deployment files in {OUTPUT}...")
        shutil.rmtree(OUTPUT)
    os.makedirs(OUTPUT, exist_ok=True)
    
    # 3. Copy Compiled Assets from dist
    print("\nCopying compiled assets from dist/...")
    # Copy index.html
    safe_copy(os.path.join(DIST, "index.html"), os.path.join(OUTPUT, "index.html"))
    # Copy assets folder (JS, CSS, chunks)
    os.makedirs(os.path.join(OUTPUT, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(DIST, "assets")):
        safe_copy(os.path.join(DIST, "assets", f), os.path.join(OUTPUT, "assets", f))
    
    # 4. Copy JSON Database Files
    print("\nCopying JSON database files...")
    for jf in JSON_FILES:
        src = os.path.join(ROOT, jf)
        if os.path.exists(src):
            safe_copy(src, os.path.join(OUTPUT, jf))
            print(f"  ✓ Copied {jf}")
        else:
            print(f"  ⚠ Warning: {jf} not found in root")
            
    # 5. Copy Markdown Reading Modules
    print("\nCopying Markdown reading modules (.md)...")
    copied_mds = 0
    for f in os.listdir(ROOT):
        if f.endswith(".md") and not f.startswith("walkthrough") and not f.startswith("implementation_plan"):
            safe_copy(os.path.join(ROOT, f), os.path.join(OUTPUT, f))
            copied_mds += 1
    print(f"  ✓ Copied {copied_mds} markdown files")

    # 6. Copy Configuration Files
    print("\nCopying configuration and SEO files...")
    for cf in CONFIG_FILES:
        src = os.path.join(ROOT, cf)
        if os.path.exists(src):
            safe_copy(src, os.path.join(OUTPUT, cf))
            print(f"  ✓ Copied {cf}")
        else:
            print(f"  ⚠ Warning: {cf} not found in root")

    # 7. Create empty 'imagenes' directory as requested
    os.makedirs(os.path.join(OUTPUT, "imagenes"), exist_ok=True)
    print("  ✓ Created empty 'imagenes/' directory")

    # 8. Copy Media Files (using hardlinks for speed and zero-space duplication)
    print("\nLinking media files (.mp4, .mp3) for self-contained deployment...")
    copied_mp4s = 0
    copied_mp3s = 0
    for f in os.listdir(ROOT):
        ext = os.path.splitext(f)[1].lower()
        if ext in ('.mp4', '.mp3'):
            src = os.path.join(ROOT, f)
            dest = os.path.join(OUTPUT, f)
            safe_copy(src, dest)
            if ext == '.mp4':
                copied_mp4s += 1
            else:
                copied_mp3s += 1
    print(f"  ✓ Processed {copied_mp4s} video files (.mp4)")
    print(f"  ✓ Processed {copied_mp3s} audio files (.mp3)")

    print("\n==========================================")
    print("  Ferozo Build & Packaging Complete!")
    print("==========================================")
    print(f"  Production directory ready at: {OUTPUT}")
    print("  You can upload the contents of this folder directly to your FTP server under /public_html/splus/")
    print("==========================================")

if __name__ == "__main__":
    main()
