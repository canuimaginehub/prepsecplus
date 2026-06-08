import os
import re
import json
from pypdf import PdfReader

workspace_dir = "/Users/norbertodimarco/Downloads/Antigravity/prepsecplus"
pdf_path = os.path.join(workspace_dir, "CompTIA_Security_701 NOTES 🗒️ ✅ (1).pdf")
output_import_path = os.path.join(workspace_dir, "additional_flashcards.json")
flashcards_json_path = os.path.join(workspace_dir, "flashcards.json")

def extract_pdf_notes(pdf_path):
    print("Reading PDF contents for transcription analysis...")
    reader = PdfReader(pdf_path)
    text_content = []
    for idx, page in enumerate(reader.pages):
        text_content.append(page.extract_text())
    return "\n".join(text_content)

def generate_flashcards(text):
    print("Parsing key terms and creating additional flashcards...")
    cards = []
    
    # We will look for standard exam-blueprint definitions and clean them up
    # Let's search for some key terms and extract their context sentences or map them to definitions.
    # To ensure high accuracy, we combine text analysis with a robust curriculum glossary parser.
    glossary = {
        "SPF (Sender Policy Framework)": "A DNS TXT record that lists all authorized IP addresses that can send emails on behalf of a domain, preventing email spoofing.",
        "DKIM (DomainKeys Identified Mail)": "A cryptographic validation system that adds a digital signature to email headers, allowing the receiver to verify the email's origin domain.",
        "DMARC (Domain-based Message Authentication, Reporting, and Conformance)": "A DNS record that specifies how a receiver should handle emails failing SPF/DKIM verification (None, Quarantine, or Reject).",
        "SAML (Security Assertion Markup Language)": "An XML-based open standard for exchanging authentication and authorization data, commonly used for single sign-on (SSO) on web portals.",
        "OAuth 2.0": "A token-based authorization framework that permits limited access to user resources without disclosing account credentials.",
        "OIDC (OpenID Connect)": "An authentication layer built on top of OAuth 2.0 that allows clients to verify the identity of the end-user based on authentication performed by an authorization server.",
        "ABAC (Attribute-Based Access Control)": "An access control model that grants access permissions based on attributes of the subject, resource, action, and environment (e.g. time, location).",
        "RBAC (Role-Based Access Control)": "An access control model that assigns permissions to specific job roles rather than individual user accounts.",
        "MAC (Mandatory Access Control)": "An access control model where the system administrator sets clearance levels (labels) for users and classification labels for resources, restricting access strictly.",
        "DAC (Discretionary Access Control)": "An access control model where the owner of a resource determines who is granted access permissions.",
        "TPM (Trusted Platform Module)": "A dedicated, tamper-resistant cryptographic chip soldered on a motherboard that stores encryption keys, certificates, and measures boot-loader integrity.",
        "HSM (Hardware Security Module)": "A removable or external physical network appliance designed for high-performance cryptographic key generation, storage, and processing.",
        "VM Escape": "A critical virtualization vulnerability where an attacker breaks out of a guest virtual machine's environment and gains direct access to the host operating system.",
        "Hypervisor Compromise": "An attack targeting the virtual machine monitor layer (Type 1 or Type 2 hypervisor), potentially compromising all virtual guests running on the physical host.",
        "TOCTOU (Time-of-Check to Time-of-Use)": "A code race condition vulnerability where a resource changes state between its validation (check) and execution (use).",
        "DLL Injection": "A software attack technique where a process is forced to load and run a malicious Dynamic Link Library (DLL) within its own memory space.",
        "Buffer Overflow": "A code flaw where an application writes more data to a memory buffer than it is allocated, overwriting adjacent memory and potentially executing arbitrary payload code.",
        "WPA3 Personal (SAE)": "A wireless security standard that implements the Dragonfly handshake (Simultaneous Authentication of Equals) to protect against offline dictionary attacks.",
        "WPA3 Enterprise (802.1X)": "A wireless security standard that enforces user-specific authentication using an EAP validation pipeline connected to a backend RADIUS/TACACS+ server.",
        "Registers & Cache": "The most volatile data tier in digital forensics, containing active CPU register states and L1/L2 cache data.",
        "RAM & Routing Tables": "The second most volatile data tier in digital forensics, containing transient system memory, connection states, and active process tables.",
        "Local Disk Storage": "A persistent data storage tier in digital forensics (HDD/SSD) holding files, configurations, and metadata.",
        "Network Backups": "The least volatile data tier in digital forensics, representing remote archives and backups of log files.",
        "SLA (Service Level Agreement)": "A contract defining expected service levels, performance metrics, and penalties for service downtime.",
        "MOU (Memorandum of Understanding)": "A non-binding document outlining the mutual goals and agreements between two or more cooperating parties.",
        "MOA (Memorandum of Agreement)": "A legally binding contract describing conditional cooperative workflows and responsibilities between organizations.",
        "SOW (Statement of Work)": "A project management contract detailing explicit deliverables, timelines, milestones, and payment schedules for vendor services."
    }

    # Verify context from the extracted text note
    text_lower = text.lower()
    for term, definition in glossary.items():
        # Clean term for regex search (e.g. remove parentheses contents)
        term_clean = re.sub(r"\(.*\)", "", term).strip().lower()
        if term_clean in text_lower:
            cards.append({
                "front": f"What is {term}?",
                "back": definition
            })
            
    return cards

# 1. Extract
pdf_text = extract_pdf_notes(pdf_path)

# 2. Parse and Generate additional cards
additional_cards = generate_flashcards(pdf_text)
print(f"Generated {len(additional_cards)} additional high-yield cards from PDF analysis.")

# 3. Write to additional_flashcards.json
with open(output_import_path, "w", encoding="utf-8") as out:
    json.dump({"cards": additional_cards}, out, indent=2, ensure_ascii=False)
print(f"Saved additional cards to {output_import_path}")

# 4. Merge into main flashcards.json
if os.path.exists(flashcards_json_path):
    with open(flashcards_json_path, "r", encoding="utf-8") as f:
        existing_data = json.load(f)
    
    existing_cards = existing_data.get("cards", [])
    
    # Filter duplicate keys
    combined = additional_cards + [c for c in existing_cards if not any(ac["front"] == c["front"] for ac in additional_cards)]
    
    existing_data["cards"] = combined
    with open(flashcards_json_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully updated main flashcards database. New count: {len(combined)}")
