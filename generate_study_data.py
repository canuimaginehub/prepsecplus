#!/usr/bin/env python3
"""
generate_study_data.py
Generates study_days.json, domains.json, and exam_objectives.json
by combining existing schedule, video, flashcard, and question data.
"""
import json
import os
import random

ROOT = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────
# 1. Hardcoded SY0-701 Exam Objectives (parsed from official CompTIA doc)
# ──────────────────────────────────────────────
EXAM_OBJECTIVES = [
    {
        "code": "1.1",
        "title": "Compare and contrast various types of security controls",
        "domain_id": "domain_1",
        "bullets": [
            "Categories: Technical, Managerial, Operational, Physical",
            "Control types: Preventive, Deterrent, Detective, Corrective, Compensating, Directive"
        ]
    },
    {
        "code": "1.2",
        "title": "Summarize fundamental security concepts",
        "domain_id": "domain_1",
        "bullets": [
            "Confidentiality, Integrity, and Availability (CIA)",
            "Non-repudiation",
            "Authentication, Authorization, and Accounting (AAA) — authenticating people, systems; authorization models",
            "Gap analysis",
            "Zero Trust — Control Plane (Adaptive identity, Threat scope reduction, Policy-driven access control, Policy Administrator, Policy Engine), Data Plane (Implicit trust zones, Subject/System, Policy Enforcement Point)",
            "Physical security — Bollards, Access control vestibule, Fencing, Video surveillance, Security guard, Access badge, Lighting, Sensors (Infrared, Pressure, Microwave, Ultrasonic)",
            "Deception and disruption technology — Honeypot, Honeynet, Honeyfile, Honeytoken"
        ]
    },
    {
        "code": "1.3",
        "title": "Explain the importance of change management processes and the impact to security",
        "domain_id": "domain_1",
        "bullets": [
            "Business processes impacting security operation — Approval process, Ownership, Stakeholders, Impact analysis, Test results, Backout plan, Maintenance window, Standard operating procedure",
            "Technical implications — Allow lists/deny lists, Restricted activities, Downtime, Service restart, Application restart, Legacy applications, Dependencies",
            "Documentation — Updating diagrams, Updating policies/procedures, Version control"
        ]
    },
    {
        "code": "1.4",
        "title": "Explain the importance of using appropriate cryptographic solutions",
        "domain_id": "domain_1",
        "bullets": [
            "Public key infrastructure (PKI) — Public key, Private key, Key escrow",
            "Encryption — Level (Full-disk, Partition, File, Volume, Database, Record), Transport/communication, Asymmetric, Symmetric, Key exchange, Algorithms, Key length",
            "Tools — TPM, HSM, Key management system, Secure enclave",
            "Obfuscation — Steganography, Tokenization, Data masking",
            "Hashing — Salting, Digital signatures, Key stretching",
            "Blockchain — Open public ledger",
            "Certificates — Certificate authorities, CRLs, OCSP, Self-signed, Third-party, Root of trust, CSR generation, Wildcard"
        ]
    },
    {
        "code": "2.1",
        "title": "Compare and contrast common threat actors and motivations",
        "domain_id": "domain_2",
        "bullets": [
            "Threat actors — Nation-state, Unskilled attacker, Hacktivist, Insider threat, Organized crime, Shadow IT",
            "Attributes of actors — Internal/external, Resources/funding, Level of sophistication/capability",
            "Motivations — Data exfiltration, Espionage, Service disruption, Blackmail, Financial gain, Philosophical/political beliefs, Ethical, Revenge, Disruption/chaos, War"
        ]
    },
    {
        "code": "2.2",
        "title": "Explain common threat vectors and attack surfaces",
        "domain_id": "domain_2",
        "bullets": [
            "Message-based — Email, SMS, Instant messaging (IM)",
            "Image-based, File-based, Voice call, Removable device",
            "Vulnerable software — Client-based vs. agentless, Unsupported systems and applications",
            "Unsecure networks — Wireless, Wired, Bluetooth",
            "Open service ports, Default credentials",
            "Supply chain — MSPs, Vendors, Suppliers",
            "Human vectors/social engineering — Phishing, Vishing, Smishing, Misinformation/disinformation, Impersonation, Business email compromise, Pretexting, Watering hole, Brand impersonation, Typosquatting"
        ]
    },
    {
        "code": "2.3",
        "title": "Explain various types of vulnerabilities",
        "domain_id": "domain_2",
        "bullets": [
            "Application — Memory injection, Buffer overflow, Race conditions (TOC/TOU), Malicious update",
            "Operating system (OS)-based",
            "Web-based — SQL injection (SQLi), Cross-site scripting (XSS)",
            "Hardware — Firmware, End-of-life, Legacy",
            "Virtualization — VM escape, Resource reuse",
            "Cloud-specific, Supply chain (Service/Hardware/Software provider), Cryptographic, Misconfiguration",
            "Mobile device — Side loading, Jailbreaking",
            "Zero-day"
        ]
    },
    {
        "code": "2.4",
        "title": "Given a scenario, analyze indicators of malicious activity",
        "domain_id": "domain_2",
        "bullets": [
            "Malware attacks — Ransomware, Trojan, Worm, Spyware, Bloatware, Virus, Keylogger, Logic bomb, Rootkit",
            "Physical attacks — Brute force, RFID cloning, Environmental",
            "Network attacks — DDoS (Amplified, Reflected), DNS attacks, Wireless, On-path, Credential replay",
            "Malicious code, Application attacks — Injection, Buffer overflow, Replay, Privilege escalation, Forgery, Directory traversal",
            "Cryptographic attacks — Downgrade, Collision, Birthday",
            "Password attacks — Spraying, Brute force",
            "Indicators — Account lockout, Concurrent session usage, Blocked content, Impossible travel, Resource consumption, Resource inaccessibility, Out-of-cycle logging, Published/documented, Missing logs"
        ]
    },
    {
        "code": "2.5",
        "title": "Explain the purpose of mitigation techniques used to secure the enterprise",
        "domain_id": "domain_2",
        "bullets": [
            "Segmentation, Access control — ACL, Permissions",
            "Application allow list, Isolation, Patching, Encryption, Monitoring, Least privilege, Configuration enforcement, Decommissioning",
            "Hardening techniques — Encryption, Endpoint protection, Host-based firewall, HIPS, Disabling ports/protocols, Default password changes, Removal of unnecessary software"
        ]
    },
    {
        "code": "3.1",
        "title": "Compare and contrast security implications of different architecture models",
        "domain_id": "domain_3",
        "bullets": [
            "Cloud — Responsibility matrix, Hybrid considerations, Third-party vendors",
            "Infrastructure as code (IaC), Serverless, Microservices",
            "Network infrastructure — Physical isolation (Air-gapped), Logical segmentation, SDN",
            "On-premises, Centralized vs. decentralized, Containerization, Virtualization",
            "IoT, ICS/SCADA, RTOS, Embedded systems, High availability",
            "Considerations — Availability, Resilience, Cost, Responsiveness, Scalability, Ease of deployment, Risk transference, Ease of recovery, Patch availability, Inability to patch, Power, Compute"
        ]
    },
    {
        "code": "3.2",
        "title": "Given a scenario, apply security principles to secure enterprise infrastructure",
        "domain_id": "domain_3",
        "bullets": [
            "Infrastructure considerations — Device placement, Security zones, Attack surface, Connectivity, Failure modes (Fail-open, Fail-closed), Device attribute (Active vs. passive, Inline vs. tap/monitor)",
            "Network appliances — Jump server, Proxy server, IPS/IDS, Load balancer, Sensors",
            "Port security — 802.1X, EAP",
            "Firewall types — WAF, UTM, NGFW, Layer 4/Layer 7",
            "Secure communication/access — VPN, Remote access, Tunneling, TLS, IPSec, SD-WAN, SASE",
            "Selection of effective controls"
        ]
    },
    {
        "code": "3.3",
        "title": "Compare and contrast concepts and strategies to protect data",
        "domain_id": "domain_3",
        "bullets": [
            "Data types — Regulated, Trade secret, Intellectual property, Legal information, Financial information, Human- and non-human-readable",
            "Data classifications — Sensitive, Confidential, Public, Restricted, Private, Critical",
            "General data considerations — Data states (Data at rest, Data in transit, Data in use), Data sovereignty, Geolocation",
            "Methods to secure data — Geographic restrictions, Encryption, Hashing, Masking, Tokenization, Obfuscation, Segmentation, Permission restrictions"
        ]
    },
    {
        "code": "3.4",
        "title": "Explain the importance of resilience and recovery in security architecture",
        "domain_id": "domain_3",
        "bullets": [
            "High availability — Load balancing vs. clustering",
            "Site considerations — Hot, Cold, Warm, Geographic dispersion",
            "Platform diversity, Multi-cloud systems",
            "Continuity of operations — Capacity planning (People, Technology, Infrastructure)",
            "Testing — Tabletop exercises, Fail over, Simulation, Parallel processing",
            "Backups — Onsite/offsite, Frequency, Encryption, Snapshots, Recovery, Replication, Journaling",
            "Power — Generators, UPS"
        ]
    },
    {
        "code": "4.1",
        "title": "Given a scenario, apply common security techniques to computing resources",
        "domain_id": "domain_4",
        "bullets": [
            "Secure baselines — Establish, Deploy, Maintain",
            "Hardening targets — Mobile devices, Workstations, Switches, Routers, Cloud infrastructure, Servers, ICS/SCADA, Embedded systems, RTOS, IoT devices",
            "Wireless devices — Installation considerations, Site surveys, Heat maps",
            "Mobile solutions — MDM, Deployment models (BYOD, COPE, CYOD), Connection methods (Cellular, Wi-Fi, Bluetooth)",
            "Wireless security settings — WPA3, AAA/RADIUS, Cryptographic protocols, Authentication protocols",
            "Application security — Input validation, Secure cookies, Static code analysis, Code signing, Sandboxing, Monitoring"
        ]
    },
    {
        "code": "4.2",
        "title": "Explain the security implications of proper hardware, software, and data asset management",
        "domain_id": "domain_4",
        "bullets": [
            "Acquisition/procurement process",
            "Assignment/accounting — Ownership, Classification",
            "Monitoring/asset tracking — Inventory, Enumeration",
            "Disposal/decommissioning — Sanitization, Destruction, Certification",
            "Data retention"
        ]
    },
    {
        "code": "4.3",
        "title": "Explain various activities associated with vulnerability management",
        "domain_id": "domain_4",
        "bullets": [
            "Identification methods — Vulnerability scan, Application security (Static/Dynamic analysis), Package monitoring",
            "Threat feed — OSINT, Proprietary/third-party, Information-sharing organization, Dark web",
            "Penetration testing, Responsible disclosure program, Bug bounty program, System/process audit",
            "Analysis — Confirmation, False positive, False negative, Prioritize (CVSS, CVE), Vulnerability classification, Exposure factor, Environmental variables, Industry/organizational impact, Risk tolerance",
            "Vulnerability response and remediation — Patching, Insurance, Segmentation, Compensating controls, Exceptions and exemptions",
            "Validation of remediation — Rescanning, Audit, Verification, Reporting"
        ]
    },
    {
        "code": "4.4",
        "title": "Explain security alerting and monitoring concepts and tools",
        "domain_id": "domain_4",
        "bullets": [
            "Monitoring computing resources — Systems, Applications, Infrastructure",
            "Activities — Log aggregation, Alerting, Scanning, Reporting, Archiving",
            "Alert response and remediation/validation — Quarantine, Alert tuning",
            "Tools — SCAP, Benchmarks, Agents/agentless, SIEM, Antivirus, DLP, SNMP traps, NetFlow, Vulnerability scanners"
        ]
    },
    {
        "code": "4.5",
        "title": "Given a scenario, modify enterprise capabilities to enhance security",
        "domain_id": "domain_4",
        "bullets": [
            "Firewall — Rules, Access lists, Ports/protocols, Screened subnets",
            "IDS/IPS — Trends, Signatures",
            "Web filter — Agent-based, Centralized proxy, URL scanning, Content categorization, Block rules, Reputation",
            "Operating system security — Group Policy, SELinux",
            "Implementation of secure protocols — Protocol selection, Port selection, Transport method",
            "DNS filtering, Email security — DMARC, DKIM, SPF, Gateway",
            "File integrity monitoring, DLP, NAC, EDR/XDR, User behavior analytics"
        ]
    },
    {
        "code": "4.6",
        "title": "Given a scenario, implement and maintain identity and access management",
        "domain_id": "domain_4",
        "bullets": [
            "Provisioning/de-provisioning user accounts, Permission assignments and implications",
            "Identity proofing, Federation, Single sign-on (SSO) — LDAP, OAuth, SAML",
            "Interoperability, Attestation",
            "Access controls — Mandatory, Discretionary, Role-based, Rule-based, Attribute-based, Time-of-day restrictions, Least privilege",
            "Multifactor authentication — Implementations (Biometrics, Hard/soft authentication tokens, Security keys), Factors (Something you know/have/are, Somewhere you are)",
            "Password concepts — Best practices (Length, Complexity, Reuse, Expiration, Age), Password managers, Passwordless",
            "Privileged access management tools — Just-in-time permissions, Password vaulting, Ephemeral credentials"
        ]
    },
    {
        "code": "4.7",
        "title": "Explain the importance of automation and orchestration related to secure operations",
        "domain_id": "domain_4",
        "bullets": [
            "Use cases of automation and scripting — User provisioning, Resource provisioning, Guard rails, Security groups, Ticket creation, Escalation, Enabling/disabling services and access",
            "Continuous integration and testing, Integrations and APIs",
            "Benefits — Efficiency/time saving, Enforcing baselines, Standard infrastructure configurations, Scaling in a secure manner, Employee retention, Reaction time, Workforce multiplier",
            "Other considerations — Complexity, Cost, Single point of failure, Technical debt, Ongoing supportability"
        ]
    },
    {
        "code": "4.8",
        "title": "Explain appropriate incident response activities",
        "domain_id": "domain_4",
        "bullets": [
            "Process — Preparation, Detection, Analysis, Containment, Eradication, Recovery, Lessons learned",
            "Training, Testing — Tabletop exercise, Simulation",
            "Root cause analysis, Threat hunting",
            "Digital forensics — Legal hold, Chain of custody, Acquisition, Reporting, Preservation, E-discovery"
        ]
    },
    {
        "code": "4.9",
        "title": "Given a scenario, use data sources to support an investigation",
        "domain_id": "domain_4",
        "bullets": [
            "Log data — Firewall logs, Application logs, Endpoint logs, OS-specific security logs, IPS/IDS logs, Network logs, Metadata",
            "Data sources — Vulnerability scans, Automated reports, Dashboards, Packet captures"
        ]
    },
    {
        "code": "5.1",
        "title": "Summarize elements of effective security governance",
        "domain_id": "domain_5",
        "bullets": [
            "Guidelines, Policies — AUP, Information security policies, Business continuity, Disaster recovery, Incident response, SDLC, Change management",
            "Standards — Password, Access control, Physical security, Encryption",
            "Procedures — Change management, Onboarding/offboarding, Playbooks",
            "External considerations — Regulatory, Legal, Industry, Local/regional, National, Global",
            "Monitoring and revision",
            "Types of governance structures — Boards, Committees, Government entities, Centralized/decentralized",
            "Roles and responsibilities for systems and data — Owners, Controllers, Processors, Custodians/stewards"
        ]
    },
    {
        "code": "5.2",
        "title": "Explain elements of the risk management process",
        "domain_id": "domain_5",
        "bullets": [
            "Risk identification, Risk assessment — Ad hoc, Recurring, One-time, Continuous",
            "Risk analysis — Qualitative, Quantitative (SLE, ALE, ARO, Probability, Likelihood, Exposure factor, Impact)",
            "Risk register — Key risk indicators, Risk owners, Risk threshold, Risk tolerance, Risk appetite (Expansionary, Conservative, Neutral)",
            "Risk management strategies — Transfer, Accept, Exemption, Exception, Avoid, Mitigate",
            "Risk reporting, Business impact analysis — RTO, RPO, MTTR, MTBF"
        ]
    },
    {
        "code": "5.3",
        "title": "Explain the processes associated with third-party risk assessment and management",
        "domain_id": "domain_5",
        "bullets": [
            "Vendor assessment — Penetration testing, Right-to-audit clause, Evidence of internal audits, Independent assessments, Supply chain analysis",
            "Vendor selection — Due diligence, Conflict of interest",
            "Agreement types — SLA, MOA, MOU, MSA, WO/SOW, NDA, BPA",
            "Vendor monitoring, Questionnaires, Rules of engagement"
        ]
    },
    {
        "code": "5.4",
        "title": "Summarize elements of effective security compliance",
        "domain_id": "domain_5",
        "bullets": [
            "Compliance reporting — Internal, External",
            "Consequences of non-compliance — Fines, Sanctions, Reputational damage, Loss of license, Contractual impacts",
            "Compliance monitoring — Due diligence/care, Attestation and acknowledgement, Internal and external, Automation",
            "Privacy — Legal implications (Local/regional, National, Global), Data subject, Controller vs. processor, Ownership, Data inventory and retention, Right to be forgotten"
        ]
    },
    {
        "code": "5.5",
        "title": "Explain types and purposes of audits and assessments",
        "domain_id": "domain_5",
        "bullets": [
            "Attestation — Internal (Compliance, Audit committee, Self-assessments), External (Regulatory, Examinations, Assessment, Independent third-party audit)",
            "Penetration testing — Physical, Offensive, Defensive, Integrated",
            "Known environment, Partially known environment, Unknown environment",
            "Reconnaissance — Passive, Active"
        ]
    },
    {
        "code": "5.6",
        "title": "Given a scenario, implement security awareness practices",
        "domain_id": "domain_5",
        "bullets": [
            "Phishing — Campaigns, Recognizing a phishing attempt, Responding to reported suspicious messages",
            "Anomalous behavior recognition — Risky, Unexpected, Unintentional",
            "User guidance and training — Policy/handbooks, Situational awareness, Insider threat, Password management, Removable media and cables, Social engineering, Operational security, Hybrid/remote work environments",
            "Reporting and monitoring — Initial, Recurring",
            "Development, Execution"
        ]
    }
]

# ──────────────────────────────────────────────
# 2. Domain definitions
# ──────────────────────────────────────────────
DOMAIN_DEFS = {
    "domain_1": {
        "title": "1.0 General Security Concepts",
        "weight": "12%",
        "description": "Foundational security principles including control types, CIA triad, zero trust architecture, change management, and cryptographic solutions.",
        "color": "cyan",
        "sub_objectives": ["1.1", "1.2", "1.3", "1.4"],
        "day_range": [1, 4]
    },
    "domain_2": {
        "title": "2.0 Threats, Vulnerabilities, and Mitigations",
        "weight": "22%",
        "description": "Threat actors, attack vectors, software/hardware vulnerabilities, malware indicators, network attacks, and enterprise mitigation techniques.",
        "color": "purple",
        "sub_objectives": ["2.1", "2.2", "2.3", "2.4", "2.5"],
        "day_range": [5, 10]
    },
    "domain_3": {
        "title": "3.0 Security Architecture",
        "weight": "18%",
        "description": "Cloud and hybrid architecture models, network infrastructure security, data protection strategies, and resilience/recovery design.",
        "color": "pink",
        "sub_objectives": ["3.1", "3.2", "3.3", "3.4"],
        "day_range": [11, 15]
    },
    "domain_4": {
        "title": "4.0 Security Operations",
        "weight": "28%",
        "description": "Secure baselines, asset management, vulnerability management, monitoring, IAM, automation, incident response, and forensics.",
        "color": "amber",
        "sub_objectives": ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9"],
        "day_range": [16, 23]
    },
    "domain_5": {
        "title": "5.0 Security Program Management and Oversight",
        "weight": "20%",
        "description": "Security governance, risk management processes, third-party assessments, compliance frameworks, audits, and security awareness training.",
        "color": "green",
        "sub_objectives": ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6"],
        "day_range": [24, 28]
    }
}

# Map sub-objectives to domain IDs
SUB_TO_DOMAIN = {}
for did, ddef in DOMAIN_DEFS.items():
    for sub in ddef["sub_objectives"]:
        SUB_TO_DOMAIN[sub] = did

# Map domain names (from questions.json) to domain IDs
DOMAIN_NAME_MAP = {
    "General Security Concepts": "domain_1",
    "Threats, Vulnerabilities, and Mitigations": "domain_2",
    "Security Architecture": "domain_3",
    "Security Operations": "domain_4",
    "Security Program Management and Oversight": "domain_5"
}

# ──────────────────────────────────────────────
# 3. Topic name map (day -> human readable topic)
# ──────────────────────────────────────────────
DAY_TOPIC_MAP = {
    1: "Security Controls",
    2: "Security Concepts & ZTA",
    3: "Change Management",
    4: "Cryptographic PKI",
    5: "Threat Actors",
    6: "Threat Vectors & Social Engineering",
    7: "Software & Hardware Vulnerabilities",
    8: "Indicators of Compromise — Malware",
    9: "Network & Application Attacks",
    10: "Mitigation & Hardening Techniques",
    11: "Cloud Models & Architecture",
    12: "Secure Infrastructure & Firewalls",
    13: "Data Protection & Classification",
    14: "Resilience, Backups & Recovery",
    15: "Domain 3 Architecture Review",
    16: "Secure Baselines & Wireless",
    17: "Asset & Vulnerability Management",
    18: "Security Monitoring & Logging",
    19: "Secure Protocols & Ports",
    20: "Identity & Access Management",
    21: "Automation & Scripting",
    22: "Incident Response & Forensics",
    23: "Data Sources & Investigation",
    24: "Security Governance & Policies",
    25: "Risk Management & Calculations",
    26: "Third-Party Vendor Contracts",
    27: "Audits & Assessments",
    28: "Security Awareness Training",
    29: "Full Exam Simulation — Review D1 & D2",
    30: "Full Exam Simulation — Review D3",
    31: "Full Exam Simulation — Review D4",
    32: "Full Exam Simulation — Review D5",
    33: "Full Exam Simulation — All Domains",
    34: "Exam Day Warm-up & Final Prep"
}


def get_domain_for_day(day_num):
    """Return domain_id for a given day number."""
    if day_num <= 4:
        return "domain_1"
    elif day_num <= 10:
        return "domain_2"
    elif day_num <= 15:
        return "domain_3"
    elif day_num <= 23:
        return "domain_4"
    elif day_num <= 28:
        return "domain_5"
    else:
        return None  # review days


def load_json(filename):
    path = os.path.join(ROOT, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filename, data):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Saved {filename} ({os.path.getsize(path):,} bytes)")


def main():
    print("═══════════════════════════════════════════")
    print("  SecPlus Study Data Generator")
    print("═══════════════════════════════════════════\n")

    # ── Load existing data ──
    print("Loading existing data files...")
    schedule = load_json("schedule.json")
    videos = load_json("videos.json")
    questions = load_json("questions.json")
    flashcards_raw = load_json("flashcards.json")
    flashcards = flashcards_raw.get("cards", [])

    print(f"  Schedule: {len(schedule)} days")
    print(f"  Videos: {sum(len(v) for v in videos.values())} lessons across {len(videos)} sub-objectives")
    print(f"  Questions: {len(questions)} total")
    print(f"  Flashcards: {len(flashcards)} cards\n")

    # ── Index questions by domain and sub_objective ──
    qs_by_domain = {}
    qs_by_sub = {}
    for q in questions:
        dom_name = q.get("domain", "")
        dom_id = DOMAIN_NAME_MAP.get(dom_name)
        sub = q.get("sub_objective", "")
        if dom_id:
            qs_by_domain.setdefault(dom_id, []).append(q)
        if sub:
            qs_by_sub.setdefault(sub, []).append(q)

    # ── Index flashcards by rough domain matching ──
    fc_by_domain = {d: [] for d in DOMAIN_DEFS}
    domain_keywords = {
        "domain_1": ["security control", "cia", "confidentiality", "integrity", "availability", "non-repudiation", "authentication", "authorization", "accounting", "zero trust", "honeypot", "honeynet", "change management", "pki", "certificate", "encryption", "symmetric", "asymmetric", "hashing", "digital signature", "blockchain", "obfuscation", "steganography", "tpm", "hsm", "key exchange"],
        "domain_2": ["threat actor", "malware", "ransomware", "trojan", "worm", "spyware", "virus", "rootkit", "phishing", "social engineering", "buffer overflow", "sql injection", "xss", "cross-site", "ddos", "denial of service", "vulnerability", "exploit", "zero-day", "brute force", "mitigation", "hardening", "segmentation"],
        "domain_3": ["cloud", "iaas", "paas", "saas", "virtualization", "vm escape", "firewall", "waf", "load balancer", "vpn", "ipsec", "tls", "data classification", "data at rest", "data in transit", "backup", "raid", "resilience", "recovery", "high availability", "sdn"],
        "domain_4": ["wpa3", "radius", "802.1x", "siem", "log", "monitoring", "incident response", "forensics", "chain of custody", "asset management", "vulnerability scan", "penetration test", "iam", "rbac", "abac", "mac", "dac", "mfa", "sso", "ldap", "oauth", "saml", "automation", "scripting", "powershell", "bash", "python"],
        "domain_5": ["governance", "policy", "compliance", "risk management", "sle", "ale", "aro", "risk register", "sla", "mou", "moa", "nda", "audit", "assessment", "security awareness", "training", "gdpr", "hipaa", "pci"]
    }

    for card in flashcards:
        combined = (card.get("front", "") + " " + card.get("back", "")).lower()
        best_domain = None
        best_score = 0
        for dom_id, keywords in domain_keywords.items():
            score = sum(1 for kw in keywords if kw in combined)
            if score > best_score:
                best_score = score
                best_domain = dom_id
        if best_domain and best_score > 0:
            fc_by_domain[best_domain].append({
                "question": card["front"],
                "answer": card["back"]
            })
        else:
            # Default to domain_1
            fc_by_domain["domain_1"].append({
                "question": card["front"],
                "answer": card["back"]
            })

    # ════════════════════════════════════════════
    # GENERATE 1: exam_objectives.json
    # ════════════════════════════════════════════
    print("Generating exam_objectives.json...")
    save_json("exam_objectives.json", EXAM_OBJECTIVES)

    # ════════════════════════════════════════════
    # GENERATE 2: study_days.json
    # ════════════════════════════════════════════
    print("Generating study_days.json...")
    study_days = []

    for day_entry in schedule:
        day_num = day_entry["day"]
        sub_obj = day_entry["sub_objective"]
        domain_id = get_domain_for_day(day_num)
        topic = DAY_TOPIC_MAP.get(day_num, f"Day {day_num}")

        # ── Reading ref ──
        reading_ref = f"./{sub_obj}.md" if sub_obj not in ("Review", "3.0") else None
        reading_title = topic

        # For review days, use domain handout
        if day_num >= 29:
            if day_num == 29:
                reading_ref = "./Security Plus SY0-701 Domain 1 Handout.md"
                domain_id = "domain_1"
            elif day_num == 30:
                reading_ref = "./Security Plus SY0-701 Domain 3 Handout.md"
                domain_id = "domain_3"
            elif day_num == 31:
                reading_ref = "./Security Plus SY0-701 Domain 4 Handout.md"
                domain_id = "domain_4"
            elif day_num == 32:
                reading_ref = "./Security Plus SY0-701 Domain 5 Handout.md"
                domain_id = "domain_5"
            elif day_num in (33, 34):
                reading_ref = "./professor-messer-sy0-701-comptia-security-plus-course-notes-v107.md"
                domain_id = None
        elif sub_obj == "3.0":
            reading_ref = "./Security Plus SY0-701 Domain 3 Handout.md"

        # ── Video ref ──
        sub_videos = videos.get(sub_obj, [])
        video_ref = None
        video_title = None
        if sub_videos:
            video_ref = sub_videos[0]["path"]
            video_title = sub_videos[0]["title"]
        elif day_num >= 29:
            # For review days, pick a video from the review domain
            review_domain = domain_id
            if review_domain:
                for s in DOMAIN_DEFS.get(review_domain, {}).get("sub_objectives", []):
                    if s in videos and videos[s]:
                        video_ref = videos[s][0]["path"]
                        video_title = videos[s][0]["title"]
                        break

        # ── Quiz questions ──
        quiz_pool = []
        if sub_obj not in ("Review", "3.0"):
            quiz_pool = list(qs_by_sub.get(sub_obj, []))
        if domain_id and len(quiz_pool) < 15:
            domain_pool = list(qs_by_domain.get(domain_id, []))
            random.shuffle(domain_pool)
            existing_ids = {q.get("id") for q in quiz_pool}
            for q in domain_pool:
                if q.get("id") not in existing_ids and len(quiz_pool) < 15:
                    quiz_pool.append(q)
                    existing_ids.add(q.get("id"))
        # If still not enough, pull from any
        if len(quiz_pool) < 15:
            all_pool = list(questions)
            random.shuffle(all_pool)
            existing_ids = {q.get("id") for q in quiz_pool}
            for q in all_pool:
                if q.get("id") not in existing_ids and len(quiz_pool) < 15:
                    quiz_pool.append(q)
                    existing_ids.add(q.get("id"))

        random.shuffle(quiz_pool)
        quiz_questions = quiz_pool[:15]

        # ── Objective bullets ──
        obj_bullets = day_entry.get("checklist_payload", [])

        # Build the day entry
        day_data = {
            "day_id": day_num,
            "date": day_entry["date"],
            "topic": topic,
            "domain_id": domain_id,
            "sub_objective": sub_obj,
            "modules": {
                "reading": {
                    "duration_min": 20,
                    "content_ref": reading_ref,
                    "title": reading_title
                },
                "video": {
                    "duration_min": 35,
                    "content_ref": video_ref,
                    "title": video_title or topic,
                    "all_videos": [{"path": v["path"], "title": v["title"], "lesson_num": v.get("lesson_num", "01")} for v in sub_videos]
                },
                "quiz": {
                    "questions_count": len(quiz_questions),
                    "questions": quiz_questions
                }
            },
            "objectives_bullets": obj_bullets
        }
        study_days.append(day_data)

    save_json("study_days.json", study_days)

    # ════════════════════════════════════════════
    # GENERATE 3: domains.json
    # ════════════════════════════════════════════
    print("Generating domains.json...")
    domains_data = {}

    for dom_id, ddef in DOMAIN_DEFS.items():
        # Collect all videos for this domain
        dom_videos = []
        for sub in ddef["sub_objectives"]:
            for v in videos.get(sub, []):
                dom_videos.append({
                    "title": v["title"],
                    "url": v["path"],
                    "duration": "",
                    "sub_objective": sub,
                    "lesson_num": v.get("lesson_num", "01")
                })

        # Collect all readings for this domain
        dom_readings = []
        for sub in ddef["sub_objectives"]:
            md_path = f"./{sub}.md"
            if os.path.exists(os.path.join(ROOT, f"{sub}.md")):
                dom_readings.append({
                    "title": f"Sub-Objective {sub}",
                    "markdown_ref": md_path,
                    "sub_objective": sub
                })
        # Also add domain handout if exists
        handout_names = {
            "domain_1": "Security Plus SY0-701 Domain 1 Handout.md",
            "domain_2": "Security Plus SY0-701 Domain 2 HANDOUT.md",
            "domain_3": "Security Plus SY0-701 Domain 3 Handout.md",
            "domain_4": "Security Plus SY0-701 Domain 4 Handout.md",
            "domain_5": "Security Plus SY0-701 Domain 5 Handout.md"
        }
        handout = handout_names.get(dom_id)
        if handout and os.path.exists(os.path.join(ROOT, handout)):
            dom_readings.insert(0, {
                "title": f"Domain Handout — {ddef['title']}",
                "markdown_ref": f"./{handout}",
                "sub_objective": "all"
            })

        # Collect flashcards for this domain
        dom_flashcards = fc_by_domain.get(dom_id, [])

        # Collect quizzes for this domain
        dom_questions = qs_by_domain.get(dom_id, [])
        dom_quizzes = []
        # Create quiz chunks of 15 questions
        shuffled_qs = list(dom_questions)
        random.shuffle(shuffled_qs)
        for i in range(0, len(shuffled_qs), 15):
            chunk = shuffled_qs[i:i+15]
            dom_quizzes.append({
                "title": f"Quiz {i//15 + 1} — {ddef['title']}",
                "questions_count": len(chunk),
                "questions": chunk
            })

        # Get exam objectives for this domain
        dom_objectives = [obj for obj in EXAM_OBJECTIVES if obj["domain_id"] == dom_id]

        domains_data[dom_id] = {
            "id": dom_id,
            "title": ddef["title"],
            "weight": ddef["weight"],
            "description": ddef["description"],
            "color": ddef["color"],
            "sub_objectives": ddef["sub_objectives"],
            "videos": dom_videos,
            "readings": dom_readings,
            "flashcards": dom_flashcards,
            "quizzes": dom_quizzes,
            "exam_objectives": dom_objectives,
            "other_data": {
                "notes": [],
                "external_links": [
                    {"title": "CompTIA Official Exam Objectives", "url": "https://www.comptia.org/certifications/security"},
                    {"title": "Professor Messer Free Videos", "url": "https://www.professormesser.com/security-plus/sy0-701/sy0-701-video/sy0-701-comptia-security-plus-course/"}
                ],
                "files": [],
                "metadata": {
                    "total_videos": len(dom_videos),
                    "total_readings": len(dom_readings),
                    "total_flashcards": len(dom_flashcards),
                    "total_questions": len(dom_questions)
                }
            }
        }

    save_json("domains.json", domains_data)

    # ── Summary ──
    print("\n═══════════════════════════════════════════")
    print("  Generation Complete!")
    print("═══════════════════════════════════════════")
    print(f"  • exam_objectives.json: {len(EXAM_OBJECTIVES)} objectives")
    print(f"  • study_days.json: {len(study_days)} days")
    print(f"  • domains.json: {len(domains_data)} domains")
    for did, dd in domains_data.items():
        print(f"    {dd['title']}: {len(dd['videos'])} videos, {len(dd['readings'])} readings, {len(dd['flashcards'])} flashcards, {len(dd['quizzes'])} quizzes")
    print()


if __name__ == "__main__":
    main()
