import os
import zipfile
import xml.etree.ElementTree as ET
import json
import re
import html

workspace_dir = "/Users/norbertodimarco/Downloads/Antigravity/prepsecplus"
secplus_file = "/Users/norbertodimarco/Downloads/Antigravity/SecPlus"

# 1. Unescape html entities
def clean_text(text):
    if not text:
        return ""
    text = html.unescape(text)
    text = text.replace("&#x27;", "'").replace("&amp;", "&").replace("&quot;", '"')
    return text.strip()

# 2. Map XLSX Reference to Domain and Sub-Objective
def map_xlsx_ref(ref, question_text):
    ref_lower = ref.lower()
    q_lower = question_text.lower()
    
    # Defaults
    domain = "General Security Concepts"
    sub_obj = "1.1"
    
    if "controls" in ref_lower:
        sub_obj = "1.1"
        domain = "General Security Concepts"
    elif "physical security" in ref_lower or "environmental" in ref_lower:
        sub_obj = "1.2"
        domain = "General Security Concepts"
    elif "zero trust" in q_lower or "policy engine" in q_lower:
        sub_obj = "1.2"
        domain = "General Security Concepts"
    elif "cryptosystems" in ref_lower or "symmetric" in ref_lower or "asymmetric" in ref_lower or "certificate" in ref_lower:
        sub_obj = "1.4"
        domain = "General Security Concepts"
    elif "social engineering" in ref_lower or "phishing" in ref_lower:
        sub_obj = "2.2"
        domain = "Threats, Vulnerabilities, and Mitigations"
    elif "vulnerability assessments" in ref_lower or "penetration testing" in ref_lower or "vulnerability scanning" in ref_lower:
        sub_obj = "4.3"
        domain = "Security Operations"
    elif "risk assessments" in ref_lower or "risk treatment" in ref_lower or "quantitative" in ref_lower or "qualitative" in ref_lower or "sle" in q_lower or "ale" in q_lower:
        sub_obj = "5.2"
        domain = "Security Program Management and Oversight"
    elif "agreement" in ref_lower or "sla" in q_lower or "mou" in q_lower:
        sub_obj = "5.3"
        domain = "Security Program Management and Oversight"
    elif "incident response" in ref_lower or "irps" in ref_lower:
        sub_obj = "4.8"
        domain = "Security Operations"
    elif "data backup" in ref_lower or "raid" in ref_lower or "backup" in q_lower:
        sub_obj = "3.4"
        domain = "Security Architecture"
    elif "cloud" in ref_lower or "container" in ref_lower or "hypervisor" in ref_lower or "virtualization" in ref_lower:
        sub_obj = "3.1"
        domain = "Security Architecture"
    elif "firewalls" in ref_lower or "proxy" in ref_lower or "load balancing" in ref_lower or "port security" in ref_lower:
        sub_obj = "3.2"
        domain = "Security Architecture"
    elif "wi-fi" in ref_lower or "wireless" in ref_lower or "rfid" in ref_lower or "bluetooth" in ref_lower:
        sub_obj = "4.1"
        domain = "Security Operations"
    elif "data types" in ref_lower or "data classifications" in ref_lower:
        sub_obj = "3.3"
        domain = "Security Architecture"
    elif "powershell" in ref_lower or "linux shells" in ref_lower:
        sub_obj = "4.7"
        domain = "Security Operations"
    elif "identification" in ref_lower or "authentication" in ref_lower or "access control" in ref_lower or "identity" in ref_lower:
        sub_obj = "4.6"
        domain = "Security Operations"
    elif "threat actors" in ref_lower or "threat analysis" in ref_lower:
        sub_obj = "2.1"
        domain = "Threats, Vulnerabilities, and Mitigations"
    elif "weak configurations" in ref_lower or "common attacks" in ref_lower or "bots" in ref_lower or "password attacks" in ref_lower:
        sub_obj = "2.4"
        domain = "Threats, Vulnerabilities, and Mitigations"
    
    return domain, sub_obj

# 3. Parse XLSX questions
def parse_xlsx_questions(file_path):
    questions = []
    with zipfile.ZipFile(file_path) as z:
        namelist = z.namelist()
        shared_strings = []
        if "xl/sharedStrings.xml" in namelist:
            ss_content = z.read("xl/sharedStrings.xml")
            ss_root = ET.fromstring(ss_content)
            ns = {"ns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            for si in ss_root.findall(".//ns:si", ns):
                t_nodes = si.findall(".//ns:t", ns)
                text = "".join([t.text for t in t_nodes if t.text])
                shared_strings.append(text)
        
        if "xl/worksheets/sheet1.xml" in namelist:
            sheet_content = z.read("xl/worksheets/sheet1.xml")
            sheet_root = ET.fromstring(sheet_content)
            ns = {"ns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            
            rows = {}
            for row in sheet_root.findall(".//ns:row", ns):
                r_idx = int(row.get("r"))
                row_cells = {}
                for c in row.findall("ns:c", ns):
                    col_name = "".join([char for char in c.get("r") if char.isalpha()])
                    v = c.find("ns:v", ns)
                    t = c.get("t")
                    val = v.text if v is not None else ""
                    if t == "s" and val.isdigit():
                        idx = int(val)
                        val = shared_strings[idx] if idx < len(shared_strings) else val
                    row_cells[col_name] = val
                rows[r_idx] = row_cells
            
            current_q = None
            for r_idx in sorted(rows.keys()):
                row = rows[r_idx]
                b_val = row.get("B", "").strip()
                c_val = row.get("C", "").strip()
                if b_val.isdigit() and c_val:
                    if current_q:
                        questions.append(current_q)
                    ref = row.get("J", "").strip()
                    domain, sub_obj = map_xlsx_ref(ref, c_val)
                    current_q = {
                        "id": f"xlsx_{b_val}",
                        "source": "xlsx",
                        "question": clean_text(c_val),
                        "options": [
                            clean_text(row.get("D", "")),
                            clean_text(row.get("E", "")),
                            clean_text(row.get("F", "")),
                            clean_text(row.get("G", ""))
                        ],
                        "correct": clean_text(row.get("H", "")),
                        "explanation": clean_text(row.get("I", "")),
                        "reference": clean_text(ref),
                        "sub_objective": sub_obj,
                        "domain": domain
                    }
                elif current_q and not b_val and not c_val:
                    extra_exp = row.get("I", "").strip()
                    if extra_exp:
                        if current_q["explanation"]:
                            current_q["explanation"] += "\n" + clean_text(extra_exp)
                        else:
                            current_q["explanation"] = clean_text(extra_exp)
            if current_q:
                questions.append(current_q)
    return questions

# 4. Parse DOCX questions
def read_docx_paragraphs(file_path):
    with zipfile.ZipFile(file_path) as z:
        xml_content = z.read("word/document.xml")
        root = ET.fromstring(xml_content)
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        paragraphs = []
        for p in root.findall(".//w:p", ns):
            texts = [t.text for t in p.findall(".//w:t", ns) if t.text]
            paragraphs.append("".join(texts) if texts else "")
        return paragraphs

def parse_docx_questions(paragraphs):
    questions = []
    i = 0
    n = len(paragraphs)
    
    while i < n:
        line = paragraphs[i].strip()
        if line.startswith("Question ") and ("Correct" in line or "Incorrect" in line or line[9:].strip().isdigit()):
            q_num_str = line.split(" ")[1]
            q_id = "".join([c for c in q_num_str if c.isdigit()])
            
            i += 1
            while i < n and not paragraphs[i].strip():
                i += 1
            if i >= n: break
            q_text = paragraphs[i].strip()
            
            options = []
            correct_option = None
            explanations = {}
            
            i += 1
            while i < n and not paragraphs[i].strip().startswith("Overall explanation"):
                curr = paragraphs[i].strip()
                if not curr:
                    i += 1
                    continue
                
                if curr == "Your answer is correct":
                    i += 1
                    while i < n and not paragraphs[i].strip():
                        i += 1
                    if i < n:
                        correct_option = paragraphs[i].strip()
                        if correct_option not in options:
                            options.append(correct_option)
                    i += 1
                    continue
                
                if curr == "Explanation":
                    i += 1
                    while i < n and not paragraphs[i].strip():
                        i += 1
                    if i < n and options:
                        last_opt = options[-1]
                        explanations[last_opt] = paragraphs[i].strip()
                    i += 1
                    continue
                
                if curr == "Domain" or curr.startswith("Question "):
                    break
                
                if curr not in options and curr != "Your answer is incorrect" and curr != "Your answer is correct":
                    options.append(curr)
                i += 1
            
            overall_explanation = ""
            sub_objective = ""
            domain = ""
            
            if i < n and paragraphs[i].strip().startswith("Overall explanation"):
                i += 1
                while i < n and not paragraphs[i].strip():
                    i += 1
                if i < n:
                    sub_objective = paragraphs[i].strip()
                    i += 1
                    while i < n and not paragraphs[i].strip():
                        i += 1
                    if i < n:
                        overall_explanation = paragraphs[i].strip()
                i += 1
            
            while i < n:
                curr = paragraphs[i].strip()
                if curr == "Domain":
                    i += 1
                    while i < n and not paragraphs[i].strip():
                        i += 1
                    if i < n:
                        domain = paragraphs[i].strip()
                    i += 1
                    break
                if curr.startswith("Question "):
                    break
                i += 1
            
            # Map sub-objective string to code
            sub_code = "1.1"
            sub_match = re.match(r"^(\d+\.\d+)", sub_objective)
            if sub_match:
                sub_code = sub_match.group(1)
            
            # Map domain string to name
            domain_name = "General Security Concepts"
            if "1.0" in domain:
                domain_name = "General Security Concepts"
            elif "2.0" in domain:
                domain_name = "Threats, Vulnerabilities, and Mitigations"
            elif "3.0" in domain:
                domain_name = "Security Architecture"
            elif "4.0" in domain:
                domain_name = "Security Operations"
            elif "5.0" in domain:
                domain_name = "Security Program Management and Oversight"
            
            # Construct a beautiful consolidated explanation
            detailed_exps = []
            for opt, exp_t in explanations.items():
                marker = "[Correct]" if opt == correct_option else "[Incorrect]"
                detailed_exps.append(f"{marker} {opt}: {exp_t}")
            
            full_explanation = clean_text(overall_explanation) + "\n\n" + "\n".join(detailed_exps)
            
            questions.append({
                "id": f"docx_{q_id}",
                "source": "docx",
                "question": clean_text(q_text),
                "options": [clean_text(o) for o in options],
                "correct": clean_text(correct_option),
                "explanation": full_explanation,
                "reference": clean_text(sub_objective),
                "sub_objective": sub_code,
                "domain": domain_name
            })
        else:
            i += 1
            
    return questions

# 5. Parse Flashcards
def parse_flashcards(filepath):
    cards = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                front = clean_text(parts[0])
                back = clean_text(parts[1])
                cards.append({
                    "front": front,
                    "back": back
                })
    return cards

# Main execution for questions and flashcards
xlsx_path = os.path.join(workspace_dir, "Security+ (SY0-701) - Quiz Questions.xlsx")
docx_path = os.path.join(workspace_dir, "Practice Exam 1.docx")
flashcards_txt_path = os.path.join(workspace_dir, "Plain Text Flashcards.txt")

xlsx_questions = parse_xlsx_questions(xlsx_path)
docx_paragraphs = read_docx_paragraphs(docx_path)
docx_questions = parse_docx_questions(docx_paragraphs)

all_questions = xlsx_questions + docx_questions
print(f"Parsed {len(xlsx_questions)} XLSX questions and {len(docx_questions)} DOCX questions. Total: {len(all_questions)}")

all_flashcards = parse_flashcards(flashcards_txt_path)
print(f"Parsed {len(all_flashcards)} flashcards.")

# Write questions to questions.json
with open(os.path.join(workspace_dir, "questions.json"), "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

# Write flashcards to flashcards.json
flashcards_payload = {
    "deck": "SY0-701",
    "cards": all_flashcards
}
with open(os.path.join(workspace_dir, "flashcards.json"), "w", encoding="utf-8") as f:
    json.dump(flashcards_payload, f, indent=2, ensure_ascii=False)

# 6. Generate 34-day schedule data
start_date = "2026-06-08"
# Let's generate dates programmatically
import datetime
start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
dates = [(start_dt + datetime.timedelta(days=d)).strftime("%Y-%m-%d") for d in range(34)]

# Define sub-objectives and content mappings
schedule_days = []

# Domain Weights
# D1: 12% (Days 1-4)
# D2: 22% (Days 5-10)
# D3: 18% (Days 11-15)
# D4: 28% (Days 16-23)
# D5: 20% (Days 24-28)
# D1-D5 Review & Simulations: Days 29-34

daily_assignments = {
    1: {"sub_objective": "1.1", "name": "Security Control Categories and Types", "domain": "General Security Concepts", 
        "checklist": [
            "Contrast functional classifications: Preventive, Deterrent, Detective, Corrective, Compensating, and Directive controls.",
            "Map controls to contextual administrative configurations (policies, training, risk assessments).",
            "Map controls to technical systems (firewalls, encryption, antivirus).",
            "Map controls to physical barriers (gates, guards, locks, lighting)."
        ]},
    2: {"sub_objective": "1.2", "name": "Fundamental Security Concepts & Zero Trust", "domain": "General Security Concepts",
        "checklist": [
            "Define the elements of the CIA Triad (Confidentiality, Integrity, Availability).",
            "Explain non-repudiation using cryptographic mechanics (digital signatures).",
            "Contrast Identification, Authentication, Authorization, and Accounting (AAA) controls.",
            "Conduct a Gap Analysis to compare current security posture against targeted baselines.",
            "Isolate the Zero Trust Control Plane (Policy Engine & Policy Administrator) from the Data Plane (Policy Enforcement Point - PEP).",
            "Distinguish physical sensors: Infrared, Pressure, Microwave, and Ultrasonic equipment.",
            "Implement deception environments: Honeypots, Honeynets, and Honeyfiles."
        ]},
    3: {"sub_objective": "1.3", "name": "Change Management Processes", "domain": "General Security Concepts",
        "checklist": [
            "Trace the Change Control process: Request for Change (RFC), CAB approvals, scheduling, validation, and documentation.",
            "Implement technical change management constraints: rollback/backout plans and sandbox testing."
        ]},
    4: {"sub_objective": "1.4", "name": "Cryptographic Concepts and PKI Infrastructure", "domain": "General Security Concepts",
        "checklist": [
            "Audit the CSR validation pipeline from public/private key generation to Certificate Authority submission.",
            "Configure Wildcard certificate traits and specify domain matching boundaries.",
            "Detail CRL blacklists and distinguish them from real-time OCSP Stapling mechanics.",
            "Contrast symmetric vs asymmetric algorithms and check key exchange protocols (Diffie-Hellman).",
            "Evaluate hashing algorithms (SHA-256/384) and check digital signatures for integrity."
        ]},
    5: {"sub_objective": "2.1", "name": "Threat Actors, Vectors, and Motivations", "domain": "Threats, Vulnerabilities, and Mitigations",
        "checklist": [
            "Categorize threat actors: APTs, state-sponsored agents, script kiddies, hacktivists, and malicious insiders.",
            "Define threat actor motivations (financial, geopolitical, espionage, revenge)."
        ]},
    6: {"sub_objective": "2.2", "name": "Threat Vectors and Social Engineering Attacks", "domain": "Threats, Vulnerabilities, and Mitigations",
        "checklist": [
            "Detail threat vectors: email, wireless, direct access, supply chain, cloud services, and removable media.",
            "Contrast phishing, spear phishing, whaling, watering hole attacks, and impersonation."
        ]},
    7: {"sub_objective": "2.3", "name": "Software and Hardware Vulnerabilities", "domain": "Threats, Vulnerabilities, and Mitigations",
        "checklist": [
            "Map the race condition window in Time-of-Check to Time-of-Use (TOCTOU) code flaws.",
            "Identify memory manipulation tools: DLL injection vs buffer bounds checking failures.",
            "Manage hardware state transitions: End-of-Life (EOL) vs End-of-Service-Life (EOSL) assets."
        ]},
    8: {"sub_objective": "2.4", "name": "Indicators of Compromise & Network Attacks", "domain": "Threats, Vulnerabilities, and Mitigations",
        "checklist": [
            "Detect malware behaviors: Ransomware (crypto locker states), Spyware (keyloggers), Rootkits (kernel level), and Trojans.",
            "Identify physical security threats (tailgating, card cloning, dumpster diving).",
            "Analyze DoS/DDoS amplification attack vectors (DNS/NTP amplification).",
            "Isolate network attacks: On-path (MITM) attacks, ARP cache poisoning, DNS hijacking, replay attacks, and wireless threats."
        ]},
    9: {"sub_objective": "2.5", "name": "Mitigation and Hardening Techniques", "domain": "Threats, Vulnerabilities, and Mitigations",
        "checklist": [
            "Enforce security configurations: Network segmentation, VLANs, and air gapping.",
            "Configure host-level hardening: disabling unused ports/services and uninstalling default apps."
        ]},
    10: {"sub_objective": "3.1", "name": "Secure Architecture & Cloud Models", "domain": "Security Architecture",
        "checklist": [
            "Differentiate cloud deployment types: Public, Private, Hybrid, and Community clouds.",
            "Identify virtualization vulnerabilities: VM escape, hypervisor compromise, and resource exhaustion.",
            "Enforce Software-Defined Networking (SDN) security partitions."
        ]},
    11: {"sub_objective": "3.2", "name": "Securing Network Infrastructures & Firewalls", "domain": "Security Architecture",
        "checklist": [
            "Detail network appliances: firewalls, load balancers, proxies, and VPN concentrators.",
            "Contrast firewall types: stateless, stateful, Web Application Firewalls (WAF), and NGFW with DPI.",
            "Implement port-security settings (802.1X, MAC address filtering)."
        ]},
    12: {"sub_objective": "3.3", "name": "Data Types, Classifications, and Protection", "domain": "Security Architecture",
        "checklist": [
            "Contrast regulated data profiles: PII, PHI, and financial transaction records (PCI-DSS).",
            "Examine data classification tags: Public, Private, Proprietary, and Confidential.",
            "Secure states of data: data at rest (FDE), data in transit (TLS 1.3), and data in use (secure enclaves).",
            "Implement data masking, obfuscation, tokenization, and DLP policies."
        ]},
    13: {"sub_objective": "3.4", "name": "Resilience, Backups, and Recovery", "domain": "Security Architecture",
        "checklist": [
            "Design redundant systems: RAID arrays, load balancers, and active-active clustering.",
            "Evaluate backups: full, differential, incremental, and the 3-2-1 backup strategy.",
            "Differentiate recovery tests (tabletop exercises vs simulations)."
        ]},
    14: {"sub_objective": "4.1", "name": "Secure Infrastructure Baselines & Wireless Settings", "domain": "Security Operations",
        "checklist": [
            "Set secure OS baselines: firmware security (UEFI, Secure Boot) and TPM integration.",
            "Contrast secure wireless settings: WPA3 Personal using SAE Dragonfly handshakes vs WPA3 Enterprise using 802.1X/EAP validation pipelines."
        ]},
    15: {"sub_objective": "4.2", "name": "Asset Management & Disposal", "domain": "Security Operations",
        "checklist": [
            "Implement asset discovery, inventory controls, and lifecycle tracking mechanisms.",
            "Manage decommissioning processes: data sanitization, physical destruction, and disposal certifications.",
            "Establish and enforce data retention rules based on legal and organizational requirements."
        ]},
    16: {"sub_objective": "4.3", "name": "Vulnerability Management Activities", "domain": "Security Operations",
        "checklist": [
            "Detail vulnerability scanning activities: CVSS scores, remediation prioritization, and threat feeds.",
            "Differentiate static vs dynamic analysis and perform patch validation via rescanning."
        ]},
    17: {"sub_objective": "4.4", "name": "Security Monitoring and Log Aggregation", "domain": "Security Operations",
        "checklist": [
            "Deploy security log aggregation systems and detail log flow structures.",
            "Establish SIEM correlation rules to link security events across firewalls, proxies, and domain controllers."
        ]},
    18: {"sub_objective": "4.5", "name": "Secure Protocols and Port Hardening", "domain": "Security Operations",
        "checklist": [
            "Implement unencrypted service mitigation maps utilizing explicit port-level replacements: Telnet (TCP 23) to SSH (TCP 22), HTTP (TCP 80) to HTTPS (TCP 443), FTP (TCP 20/21) to SFTP (TCP 22).",
            "Hardening application ports and configuring email protections: SPF, DKIM, and DMARC DNS records."
        ]},
    19: {"sub_objective": "4.6", "name": "Identity and Access Management (IAM)", "domain": "Security Operations",
        "checklist": [
            "Contrast IAM frameworks: Directory Services (LDAP, Active Directory) and Single Sign-On (SAML, OAuth 2.0, OIDC).",
            "Enforce access control models: Attribute-based (ABAC), Role-based (RBAC), Mandatory (MAC), and Discretionary (DAC).",
            "Configure Multi-Factor Authentication (MFA) credentials: TOTP tokens, push notifications, and biometric verification."
        ]},
    20: {"sub_objective": "4.7", "name": "Scripting and Security Automation", "domain": "Security Operations",
        "checklist": [
            "Identify scripting languages: PowerShell, Bash, and Python usage for security tasks.",
            "Configure automation playbooks and deploy SOAR orchestration pipelines to accelerate incident containment."
        ]},
    21: {"sub_objective": "4.8", "name": "Incident Response & Digital Forensics", "domain": "Security Operations",
        "checklist": [
            "Map incident response steps: Preparation, Detection & Analysis, Containment, Eradication, Recovery, and Post-Incident Activity.",
            "Enforce the explicit order of data volatility across storage resources: Registers/Cache -> Routing Tables/RAM -> Local Disk Storage -> Network Backups.",
            "Trace chain of custody protocols to document evidence acquisition and hash verification."
        ]},
    22: {"sub_objective": "4.9", "name": "Analyzing Data for Security Monitoring", "domain": "Security Operations",
        "checklist": [
            "Inspect firewall connection tables, proxy logs, and DNS query histories to map malicious network telemetry.",
            "Detect data exfiltration indicators and recognize command-and-control (C2) beaconing patterns."
        ]},
    23: {"sub_objective": "5.1", "name": "Security Governance & Policies", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Differentiate governance documents: Policies (mandatory high-level), Standards (compulsory baselines), and Procedures (step-by-step instructions).",
            "Assign data handling roles: Controller, Processor, Custodian, and Owner."
        ]},
    24: {"sub_objective": "5.2", "name": "Risk Management & Calculation Formulas", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Enforce quantitative risk calculation formulas: SLE = AV * EF; ALE = ARO * SLE.",
            "Contrast recovery milestones: Recovery Time Objective (RTO timelines) vs Recovery Point Objective (RPO age tolerances).",
            "Review risk strategies: mitigation, acceptance, avoidance, and transfer."
        ]},
    25: {"sub_objective": "5.3", "name": "Third-Party Vendor Contracts & Agreements", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Examine vendor contract blueprints: Service Level Agreement (SLA), Memorandum of Understanding (MOU), Memorandum of Agreement (MOA), and Statement of Work (SOW).",
            "Identify due diligence questionnaires, right-to-audit clauses, and third-party risk assessment parameters."
        ]},
    26: {"sub_objective": "5.4", "name": "Compliance & Privacy Concepts", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Summarize privacy regulations: GDPR, HIPAA, and privacy impact assessments (PIA).",
            "Contrast controller vs processor roles and understand the right to be forgotten compliance mandate."
        ]},
    27: {"sub_objective": "5.5", "name": "Security Audits and Assessments", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Differentiate audit categories: internal audits (self-assessments) vs external audits (third-party certifications).",
            "Gather audit logs, configurations, and policy documents to validate control effectiveness."
        ]},
    28: {"sub_objective": "5.6", "name": "Security Awareness and Training", "domain": "Security Program Management and Oversight",
        "checklist": [
            "Deploy security training campaigns: phishing simulations, social engineering awareness, and clean desk policies.",
            "Measure user training effectiveness via reporting rates and click-through metrics."
        ]}
}

for i in range(1, 35):
    day_date = dates[i-1]
    
    # Track 1 rules:
    # Days 1-28: Domain-isolated drills (20 questions, 20 mins)
    # Days 29-34: Full 90-question simulations (90 questions, 90 mins)
    if i <= 28:
        # Determine domain from assignment
        asg = daily_assignments[i]
        domain_name = asg["domain"]
        t1_type = "Domain Isolated Drill"
        t1_desc = f"Domain Drill: {domain_name}. Complete 20 questions in 20 minutes focusing on Domain {asg['sub_objective'][0]}. Apply Exam Hack Rules #10 (Flag & Move) and #11 (Defer PBQ)."
        t1_qs = 20
        t1_time = 20
    else:
        domain_name = "Full Simulation"
        t1_type = "Full Exam Simulation"
        t1_desc = f"Full 90-question CompTIA Security+ practice exam simulator block. Complete under 90 minutes strict limit caps. Enforce Exam Hacks: Rule #4 (Board allocation maximization mapping), Rule #10 (Flag & Move), Rule #11 (Defer PBQs), and Rule #13 (Zero-penalty complete selection mandate)."
        t1_qs = 90
        t1_time = 90
    
    # Track 2 rules:
    if i <= 28:
        asg = daily_assignments[i]
        t2_desc = f"Study sub-objective {asg['sub_objective']}: {asg['name']}. Watch matching Professor Messer video lesson paths and read the companion reading module."
        checklist = asg["checklist"]
        sub_obj = asg["sub_objective"]
    else:
        sub_obj = "Review"
        if i == 29:
            t2_desc = "Review Domain 1 weak areas. Practice card decks on Control Classifications, CIA Triad, Zero Trust architecture, and Cryptographic PKI pipelines."
            checklist = [
                "Practice Domain 1 Flashcards (Security Control types and Zero Trust Control vs Data planes).",
                "Review PKI CSR validation pipelines and key exchange protocols.",
                "Analyze Domain 1 incorrect questions and log weak topics."
            ]
        elif i == 30:
            t2_desc = "Review Domain 2 weak areas. Practice card decks on Threat Actors, Social Engineering attacks, Malware types, and Hardening techniques."
            checklist = [
                "Practice Domain 2 Flashcards (TOCTOU race conditions, buffer overflows, injection attacks).",
                "Review indicators of compromise and mitigation methodologies.",
                "Analyze Domain 2 incorrect questions and log weak topics."
            ]
        elif i == 31:
            t2_desc = "Review Domain 3 weak areas. Drill flashcards on Cloud Deployment types, Firewall topologies, Data classifications, and Resilience configurations."
            checklist = [
                "Practice Domain 3 Flashcards (RAID configurations, differential vs incremental backups).",
                "Review states of data (TLS 1.3 transit, FDE at rest, secure enclaves in use).",
                "Analyze Domain 3 incorrect questions and log weak topics."
            ]
        elif i == 32:
            t2_desc = "Review Domain 4 weak areas. Memorize wireless settings, security baselines, vulnerability management pipelines, and port replacement maps."
            checklist = [
                "Practice Domain 4 Flashcards (WPA3 SAE, port configurations: SSH on 22, HTTPS on 443, SFTP on 22).",
                "Memorize the order of volatility (Registers -> RAM -> Disk -> Backups) and incident response phases.",
                "Analyze Domain 4 incorrect questions and log weak topics."
            ]
        elif i == 33:
            t2_desc = "Review Domain 5 weak areas. Recalculate ALE risk variables, third-party agreements, compliance regulations, and training metrics."
            checklist = [
                "Practice Domain 5 Flashcards (Risk formulas: SLE=AV*EF, ALE=ARO*SLE).",
                "Memorize agreement formats (SLA, MOU, MOA, SOW) and compliance frameworks (GDPR, HIPAA).",
                "Analyze Domain 5 incorrect questions and log weak topics."
            ]
        elif i == 34:
            t2_desc = "Comprehensive review of all 5 domains. Final memorization sweeps. Rest and mentally prepare."
            checklist = [
                "Run standard front-to-back testing flashcard deck of 200+ cards.",
                "Review high-yield acronym lists and formula sheets.",
                "Verify exam registration, location/online settings, and identification requirements.",
                "Review Exam Hack Rule #13 (Zero-penalty full selection mandate) and Rule #11 (Immediate MCQ-first routing, deferring active PBQs)."
            ]
            
    schedule_days.append({
        "day": i,
        "date": day_date,
        "sub_objective": sub_obj,
        "track_1": {
            "type": t1_type,
            "description": t1_desc,
            "questions": t1_qs,
            "time_limit": t1_time
        },
        "track_2": {
            "description": t2_desc
        },
        "checklist_payload": checklist
    })

# Write schedule to schedule.json
with open(os.path.join(workspace_dir, "schedule.json"), "w", encoding="utf-8") as f:
    json.dump(schedule_days, f, indent=2, ensure_ascii=False)

# 7. Write formatted markdown study schedule to SecPlus
with open(secplus_file, "w", encoding="utf-8") as f:
    f.write("# CompTIA Security+ (SY0-701) 34-Day High-Performance Study Plan\n\n")
    f.write("Welcome to your production-ready exam roadmap starting June 8, 2026, and running continuously until your Exam Day on July 12, 2026. This schedule enforces double-track actions and granular technical checklists for Supabase and project sync configurations.\n\n")
    
    for day in schedule_days:
        f.write(f"## Day {day['day']}: {day['date']} (Sub-Objective {day['sub_objective']})\n\n")
        
        # Track 1 Section
        f.write("### Track 1: Practice Test Engine Task\n")
        f.write(f"- [ ] **{day['track_1']['type']}** ({day['track_1']['questions']} Questions | {day['track_1']['time_limit']} Mins)\n")
        f.write(f"  {day['track_1']['description']}\n\n")
        
        # Track 2 Section
        f.write("### Track 2: Learning & Study Guide Assignment\n")
        f.write(f"- [ ] **Lesson & Module Study**\n")
        f.write(f"  {day['track_2']['description']}\n\n")
        
        # Checklist payload Section
        f.write("### Technical Checklist & Database Ingestion Payload\n")
        f.write("```json\n")
        f.write(json.dumps({"checklist_payload": day["checklist_payload"]}, indent=2))
        f.write("\n```\n")
        f.write("Checklist Actions:\n")
        for item in day["checklist_payload"]:
            f.write(f"- [ ] {item}\n")
        f.write("\n" + "-"*40 + "\n\n")
        
    f.write("## EXAM DAY: July 12, 2026\n\n")
    f.write("- [ ] **TAKE THE COMPTIA SECURITY+ EXAM (SY0-701)**\n")
    f.write("  - Enforce Exam Hack Rule #11: Immediately answer all Multiple Choice Questions first, flags enabled, delaying PBQs.\n")
    f.write("  - Enforce Exam Hack Rule #10: Flag and move on to next question if stuck. Do not spend more than 60 seconds on any single item.\n")
    f.write("  - Enforce Exam Hack Rule #4: Score maximization - align answers with the most specific control types.\n")
    f.write("  - Enforce Exam Hack Rule #13: Answer ALL questions before submitting. There is no negative grading penalty for incorrect selections.\n")

print("Successfully generated schedule.json, questions.json, flashcards.json, and wrote the study plan to /Users/norbertodimarco/Downloads/Antigravity/SecPlus.")
