import os

modules_dir = "/Users/norbertodimarco/Downloads/Antigravity/prepsecplus/modules"
os.makedirs(modules_dir, exist_ok=True)

modules = {
    "1.1": {
        "title": "Security Control Categories and Types",
        "content": """# Sub-Objective 1.1: Compare and Contrast Security Control Categories and Types

## 1. Security Control Categories
Security controls are classified into three core operational categories based on how they are implemented:
- **Technical (Logical) Controls**: Implemented through hardware, software, or firmware systems. Examples include firewalls, encryption, antivirus, Intrusion Detection/Prevention Systems (IDS/IPS), and Access Control Lists (ACLs).
- **Administrative (Managerial) Controls**: Implemented through organizational policies, guidelines, and procedures. Examples include security awareness training, employee onboarding/offboarding policies, risk assessments, and vulnerability management schedules.
- **Physical Controls**: Implemented to secure physical environments and hardware. Examples include fences, gates, barricades, guards, locks, badge readers, lighting, and security cameras.

## 2. Security Control Types
Controls are further classified by their functional purpose—what they do when protecting systems:
- **Preventive**: Designed to stop a security incident from occurring. Examples include firewalls, IPS, training, and security locks.
- **Deterrent**: Designed to discourage potential adversaries from attempting an attack. Examples include warning banners, visible security cameras, and guard dogs.
- **Detective**: Designed to identify and record security incidents as they occur or after the fact. Examples include audit logs, system alarms, motion sensors, and security reviews.
- **Corrective**: Designed to restore systems to a secure, normal operating state after an incident. Examples include backups, patch management, and system rebuilding.
- **Compensating**: Designed to provide an alternative control when a primary security measure is not feasible due to cost, technical limitations, or operational constraints.
- **Directive**: Designed to dictate behavior and compliance based on organizational rules or legal mandates. Examples include security policies and standard operating procedures (SOPs).
"""
    },
    "1.2": {
        "title": "Fundamental Security Concepts & Zero Trust",
        "content": """# Sub-Objective 1.2: Explain the Importance of Security Concepts in an Organization

## 1. The CIA Triad
- **Confidentiality**: Ensuring data is accessible only to authorized entities. Enforced using symmetric/asymmetric encryption, access controls (permissions), and data classification.
- **Integrity**: Guaranteeing that data has not been altered or tampered with. Enforced using cryptographic hashing (SHA-256) and digital signatures.
- **Availability**: Ensuring data and services are accessible when needed. Enforced using redundancy (RAID, clustering), backups, and DDoS mitigation.

## 2. Non-Repudiation
Non-repudiation prevents a party from denying an action. It is achieved through:
- **Digital Signatures**: The sender signs data with their private key, and the receiver verifies it using the sender's public key.
- **Audit Logging**: Secure, timestamped write-once logs that track user actions.

## 3. AAA Framework
- **Identification**: Declaring who you are (e.g., username, ID card).
- **Authentication**: Verifying your claimed identity (e.g., password, biometrics, MFA).
- **Authorization**: Granting specific access privileges based on authenticated identity.
- **Accounting**: Tracking and logging user actions for compliance and security reviews.

## 4. Gap Analysis
A process used to compare an organization's current security posture against target security baselines. It identifies missing controls, deficiencies, and areas requiring remediation.

## 5. Zero Trust Architecture (ZTA)
Zero Trust operates under the core principle: "Never trust, always verify."
- **Control Plane**:
  - **Policy Engine (PE)**: Makes the decision to grant or deny access based on context.
  - **Policy Administrator (PA)**: Formulates the command to establish or terminate the connection session.
- **Data Plane**:
  - **Policy Enforcement Point (PEP)**: Operates at the gateway to intercept traffic, applying the PE/PA decisions to establish or sever communication tunnels.

## 6. Physical Sensors
- **Infrared**: Detects thermal changes and infrared radiation signatures.
- **Pressure**: Detects physical weight/force changes on surfaces.
- **Microwave**: Emits microwave pulses and measures reflection shifts (Doppler effect) to detect movement.
- **Ultrasonic**: Emits high-frequency sound waves to measure room echoes for movement detection.

## 7. Deception & Disruption
- **Honeypot**: A decoy server or device designed to attract and analyze attacker behaviors.
- **Honeynet**: A network of decoy systems simulating a production subnet.
- **Honeyfile**: A decoy file configured with audit triggers to alert administrators when accessed by unauthorized users.
"""
    },
    "1.3": {
        "title": "Change Management Processes",
        "content": """# Sub-Objective 1.3: Explain the Importance of Change Management Processes

## 1. Change Control Workflow
An administrative framework designed to minimize outages and security vulnerabilities:
1. **Request for Change (RFC)**: formal documentation detailing the change's purpose, scope, and technical steps.
2. **Review & Impact Analysis**: evaluating potential side effects on operations and security.
3. **Change Advisory Board (CAB) Approval**: A review panel of stakeholders that approves or rejects changes.
4. **Sandboxed Testing**: Validation in a non-production environment.
5. **Rollback / Backout Plan**: Defining the precise steps to revert systems if the change fails.
6. **Implementation**: Deploying the change during scheduled maintenance windows.
7. **Post-Implementation Review**: Documenting success or failure and updating assets.
"""
    },
    "1.4": {
        "title": "Cryptographic Concepts and PKI Infrastructure",
        "content": """# Sub-Objective 1.4: Explain the Importance of Cryptographic Concepts and PKI

## 1. Public Key Infrastructure (PKI)
PKI manages the lifecycle of digital certificates containing public keys.
- **Certificate Authority (CA)**: The trusted entity that signs and issues certificates.
- **Certificate Signing Request (CSR)**: An application file containing a public key and identity data generated by a server, signed by the server's private key, and sent to the CA.

## 2. Certificate Types and Features
- **Wildcard Certificate**: Secures a main domain and all first-level subdomains (`*.domain.com`).
- **Subject Alternative Name (SAN)**: Secures multiple distinct domain names in a single certificate.

## 3. Revocation Mechanics
- **Certificate Revocation List (CRL)**: A list of revoked certificates published periodically by the CA. Requires clients to pull updates, causing latency.
- **Online Certificate Status Protocol (OCSP)**: A real-time request query sent to the CA to check certificate validity.
- **OCSP Stapling**: The web server periodically queries the CA for status and "staples" a time-stamped, CA-signed OCSP response to the TLS handshake, reducing CA server load and client latency.

## 4. Encryption Algorithms
- **Symmetric Encryption**: Uses the same shared key for encryption and decryption. Very fast. Examples: AES (standard), 3DES (legacy), Blowfish.
- **Asymmetric Encryption**: Uses a public-private key pair. Public key encrypts, private key decrypts (or private signs, public verifies). Used for key exchange and digital signatures. Examples: RSA, ECC (efficient for mobile), Diffie-Hellman (key exchange).

## 5. Hashing and Signatures
- **Hashing**: A one-way mathematical function generating a fixed-size digest (SHA-256). Detects integrity violations.
- **Digital Signatures**: A hashed message encrypted with the sender's private key. Provides integrity, authentication, and non-repudiation.
"""
    },
    "2.1": {
        "title": "Threat Actors, Vectors, and Motivations",
        "content": """# Sub-Objective 2.1: Compare and Contrast Common Threat Actors and Motivations

## 1. Threat Actors
- **Advanced Persistent Threat (APT)**: Sophisticated, nation-state backed actors pursuing long-term espionage or disruption. Highly funded.
- **State-Sponsored**: Nation-state agents focusing on political, military, or critical infrastructure targets.
- **Script Kiddies**: Low-skill attackers using pre-written tools. Motivated by notoriety.
- **Hacktivists**: Attackers motivated by political, ideological, or social statements.
- **Insiders**: Employees or contractors with authorized access. Can be malicious (data exfiltration) or accidental (falling for phishing).
"""
    },
    "2.2": {
        "title": "Threat Vectors and Social Engineering Attacks",
        "content": """# Sub-Objective 2.2: Compare and Contrast Common Threat Vectors and Social Engineering

## 1. Threat Vectors
- **Email**: Phishing links or attachments.
- **Wireless**: Rogue access points, intercepting unencrypted traffic.
- **Direct Access**: Physical access to consoles or networking closets.
- **Supply Chain**: Compromising third-party software updates.
- **Removable Media**: USB drops containing payload code.

## 2. Social Engineering Attacks
- **Phishing**: Mass email campaigns tricking users into disclosing info.
- **Spear Phishing**: Targeted phishing aimed at specific individuals.
- **Whaling**: Phishing targeted at high-profile executives (C-level).
- **Watering Hole**: Infecting websites commonly visited by the target group.
- **Impersonation**: Pretending to be an authority figure (IT support, executive) to gain trust.
"""
    },
    "2.3": {
        "title": "Software and Hardware Vulnerabilities",
        "content": """# Sub-Objective 2.3: Explain Common Vulnerabilities

## 1. Code Flaws and Exploits
- **Time-of-Check to Time-of-Use (TOCTOU)**: A race condition where a system validates a resource state (check) but the state changes before the resource is accessed (use).
- **DLL Injection**: Forcing a running program to execute external, malicious dynamic link libraries (DLLs) in its address space.
- **Buffer Overflow**: Sending more data to a memory buffer than it can hold, overwriting adjacent memory spaces and potentially executing arbitrary code. Mitigated by secure coding (bounds checking).

## 2. Lifecycle Vulnerabilities
- **End-of-Life (EOL)**: Hardware/software that is no longer manufactured or sold by the vendor.
- **End-of-Service-Life (EOSL)**: Hardware/software that no longer receives security updates or support from the vendor. These assets must be isolated or decommissioned immediately.
"""
    },
    "2.4": {
        "title": "Indicators of Compromise & Malware",
        "content": """# Sub-Objective 2.4: Analyze Indicators of Malicious Activity

## 1. Malware Classifications
- **Ransomware**: Encrypts files and demands payment for decryption keys.
- **Spyware & Keyloggers**: Monitors user actions and records keystrokes secretly.
- **Rootkit**: Modifies system files at the kernel level to conceal malware presence.
- **Trojan**: Disguises itself as legitimate software while carrying a malicious payload.
- **Worm**: Self-replicating malware that spreads across networks without host interaction.
- **Virus**: Malicious code that attaches itself to host files and requires execution to spread.

## 2. Network Attacks
- **DoS/DDoS Amplification**: Spoofing request packets with the victim's source IP to servers (NTP, DNS) which return significantly larger response payloads to the victim.
- **On-path (MITM)**: Intercepting and modifying network traffic between two nodes.
- **ARP Cache Poisoning**: Associating an attacker's MAC address with a target's gateway IP in local ARP tables.
- **Replay Attack**: Capturing authentication packets and re-sending them to gain unauthorized access.
"""
    },
    "2.5": {
        "title": "Mitigation and Hardening Techniques",
        "content": """# Sub-Objective 2.5: Explain Mitigation Techniques and Hardening Concepts

## 1. Network Segmentation
- **VLANs**: Logically dividing a single physical network into isolated broadcast domains.
- **Air Gapping**: Complete physical isolation of a network from all external networks.
- **Microsegmentation**: Dividing data centers into logical security zones down to individual workload levels.

## 2. System Hardening
- **Port Security**: Disabling unused switch ports.
- **Default configurations**: Changing default passwords, disabling default accounts, and removing unnecessary software.
- **Host Security**: Applying operating system updates and patches regularly.
"""
    },
    "3.1": {
        "title": "Secure Architecture & Cloud Models",
        "content": """# Sub-Objective 3.1: Compare and Contrast Security Implications of Different Architecture Models

## 1. Cloud Deployment Models
- **Public Cloud**: Shared infrastructure owned and operated by a third-party CSP.
- **Private Cloud**: Infrastructure dedicated exclusively to a single organization.
- **Hybrid Cloud**: Combines public and private clouds, sharing data and applications.
- **Community Cloud**: Shared infrastructure among organizations with common concerns (e.g., government).

## 2. Virtualization Security Risks
- **VM Escape**: An attacker exploits hypervisor bugs to break out of a guest VM to the host operating system.
- **Hypervisor Compromise**: An attack targeting the VM supervisor layer, compromising all virtual guests.
- **Resource Exhaustion**: A VM consumes all host CPU or RAM, causing a denial of service to other VMs.

## 3. Software-Defined Networking (SDN)
SDN decouples the Control Plane (routing decisions) from the Data Plane (packet forwarding). It enables granular, centralized security controls and automated network partitions.
"""
    },
    "3.2": {
        "title": "Securing Network Infrastructures & Firewalls",
        "content": """# Sub-Objective 3.2: Secure an Organization's Infrastructure

## 1. Network Appliances
- **Firewalls**: Filters traffic based on security rules.
- **Proxies**: Acts as an intermediary for client requests, caching pages and hiding client IPs.
- **Load Balancers**: Distributes traffic across multiple servers.
- **VPN Concentrators**: Handles high-volume remote-access VPN connections.

## 2. Firewall Architectures
- **Stateless Firewalls**: Evaluates individual packets against ACLs without connection context.
- **Stateful Firewalls**: Monitors connection states, automatically allowing returning traffic.
- **Web Application Firewalls (WAF)**: Inspects layer 7 HTTP traffic for application-level exploits (SQLi, XSS).
- **Next-Generation Firewalls (NGFW)**: Incorporates deep packet inspection (DPI), application awareness, and integrated IPS.

## 3. Port Security
- **802.1X**: Port-based network access control requiring RADIUS/TACACS+ authentication.
- **MAC Filtering**: Restricts access based on MAC address (easily spoofed).
"""
    },
    "3.3": {
        "title": "Data Types, Classifications, and Protection",
        "content": """# Sub-Objective 3.3: Compare and Contrast Concepts and Strategies to Protect Data

## 1. Regulated Data Profiles
- **PII (Personally Identifiable Information)**: Data identifying individuals (SSN, name).
- **PHI (Protected Health Information)**: Medical history, patient records.
- **PCI-DSS (Payment Card Industry Data Security Standard)**: Credit card transaction details.

## 2. States of Data
- **Data at Rest**: Stored on disks or tape. Secured via Full Disk Encryption (FDE) and access controls.
- **Data in Transit**: Moving across a network. Secured via TLS 1.3 or IPsec.
- **Data in Use**: Active in RAM, CPU registers, or cache. Secured via secure enclaves or homomorphic encryption.

## 3. Protection Techniques
- **Data Masking**: Replacing sensitive characters with dummy symbols (e.g., XXXXX-1234).
- **Tokenization**: Replacing sensitive data with non-sensitive placeholder tokens.
- **DLP (Data Loss Prevention)**: System that scans network egress traffic or endpoint actions to block unauthorized transfer of sensitive data.
"""
    },
    "3.4": {
        "title": "Resilience, Backups, and Recovery",
        "content": """# Sub-Objective 3.4: Explain the Importance of Resilience and Recovery in Security Architecture

## 1. Resiliency and Redundancy
- **RAID Configurations**:
  - **RAID 0**: Striping. No redundancy.
  - **RAID 1**: Mirroring. High redundancy, write penalty.
  - **RAID 5**: Striping with single parity. Tolerates 1 drive failure.
  - **RAID 6**: Striping with dual parity. Tolerates 2 drive failures.
  - **RAID 10**: Mirroring and striping combined. High performance/redundancy.
- **Clustering**: High-availability active-active or active-passive servers.

## 2. Backup Strategy
- **Full Backup**: Copies all data. High restore speed, slow backup.
- **Differential Backup**: Copies data changed since last Full backup. Moderate backup/restore speed.
- **Incremental Backup**: Copies data changed since the last backup (Full or Incremental). Fast backup, slow restore.
- **3-2-1 Strategy**: 3 copies of data, across 2 different media types, with 1 copy stored offsite.

## 3. Recovery Testing
- **Tabletop Exercises**: Discussion-based review of disaster scenarios.
- **Simulations**: Hands-on trial of restore processes in a test environment.
"""
    },
    "4.1": {
        "title": "Secure Infrastructure Baselines & Wireless Settings",
        "content": """# Sub-Objective 4.1: Secure Common Infrastructure

## 1. Host Hardening and Baselines
- **TPM (Trusted Platform Module)**: Hardware-based cryptographic chip providing secure key storage and boot integrity measurements.
- **UEFI & Secure Boot**: Verifies that bootloader code is digitally signed by trusted authorities.

## 2. Wireless Security Configurations
- **WPA3 Personal (SAE)**: Employs Simultaneous Authentication of Equals (SAE - Dragonfly handshake). Replaces WPA2 Pre-Shared Key (PSK). Provides forward secrecy and prevents offline dictionary brute-force attacks.
- **WPA3 Enterprise (802.1X)**: Integrates port-based access control (802.1X), sending client credentials to a central authentication server (RADIUS/TACACS+) via EAP (Extensible Authentication Protocol) validation pipelines.
"""
    },
    "4.2": {
        "title": "Asset Management",
        "content": """# Sub-Objective 4.2: Explain the Importance of Asset Management

## 1. Asset Inventory and Controls
- **Discovery**: Automatically scans networks to catalog active hosts and devices.
- **Lifecycle Tracking**: Monitors assets from acquisition, through deployment and maintenance, to secure decommissioning (e.g. data wiping, recycling).
- **Vulnerability Linkage**: Associates inventory items with active CVE alerts.
"""
    },
    "4.3": {
        "title": "Vulnerability Assessments & Pen Testing",
        "content": """# Sub-Objective 4.3: Analyze Vulnerability Scan Results

## 1. Vulnerability Scanning Pipelines
- **Credentialed Scans**: Uses administrative credentials to examine configuration settings, registry hives, and internal file versions. Highly accurate, few false positives.
- **Non-Credentialed Scans**: Scans externally. Mimics attacker view. High likelihood of missing deep-level flaws.

## 2. Penetration Testing Stages
- **Reconnaissance**: Gathering target info (active ports, OS types).
- **Exploitation**: Attempting to breach identified vulnerabilities.
- **Lateral Movement**: Pivoting within the network to access other hosts.
- **Cleanup**: Removing shells, user accounts, and scripts used during the test.
- **Rules of Engagement**: Document specifying test scope and times.
"""
    },
    "4.4": {
        "title": "Security Monitoring and Log Aggregation",
        "content": """# Sub-Objective 4.4: Explain the Importance of Security Monitoring and Logging

## 1. SIEM Framework
- **Log Aggregation**: Collecting log files from firewalls, servers, databases, and client endpoints into a centralized repository.
- **Event Correlation**: Linking events using predefined rules (e.g., 5 failed login attempts on a controller followed immediately by a database download) to trigger alarms.
- **SIEM Dashboards**: Real-time display of security metrics.
"""
    },
    "4.5": {
        "title": "Secure Protocols and Port Hardening",
        "content": """# Sub-Objective 4.5: Configure Secure Tools and Technologies

## 1. Service Hardening and Port Maps
To secure network infrastructure, replace unencrypted protocols with secure alternatives:
- **SSH (Port 22)**: Replaces unencrypted **Telnet (Port 23)**.
- **HTTPS (Port 443)**: Replaces unencrypted **HTTP (Port 80)**.
- **SFTP (Port 22)**: Replaces unencrypted **FTP (Ports 20/21)**.

## 2. Email Protections
- **SPF (Sender Policy Framework)**: DNS TXT record listing IP addresses authorized to send email for a domain.
- **DKIM (DomainKeys Identified Mail)**: Cryptographic signature added to email headers to verify origin domain.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**: DNS record specifying how receivers handle messages failing SPF/DKIM (Reject, Quarantine, None).
"""
    },
    "4.6": {
        "title": "Identity and Access Management (IAM)",
        "content": """# Sub-Objective 4.6: Secure Identities and Manage Access

## 1. Identity Services
- **LDAP (Port 389/636)**: Directory service protocol query format.
- **SSO (Single Sign-On)**:
  - **SAML**: XML-based protocol. Redirects authentication to Identity Provider (IdP) for web access.
  - **OAuth 2.0**: Token-based authorization protocol (uses JSON Web Tokens).
  - **OIDC (OpenID Connect)**: An authentication layer built on top of OAuth 2.0.

## 2. Access Control Models
- **RBAC (Role-Based)**: Access granted based on defined job roles (e.g., HR Specialist, DB Admin).
- **ABAC (Attribute-Based)**: Access granted based on attributes (e.g., location, time of day, department).
- **MAC (Mandatory)**: Access granted based on security clearances and labels (used in military).
- **DAC (Discretionary)**: Access granted by resource owner settings (default operating system permissions).

## 3. Multi-Factor Authentication (MFA)
Requires credentials from different factor categories:
- **Something you know** (password).
- **Something you have** (smartcard, hardware token).
- **Something you are** (biometrics).
- **Somewhere you are** (GPS coordinates).
- **Something you do** (gesture).
"""
    },
    "4.7": {
        "title": "Scripting and Security Automation",
        "content": """# Sub-Objective 4.7: Explain the Importance of Scripting and Automation in Security Operations

## 1. Scripting Environments
- **PowerShell**: Object-oriented shell used in Windows environments.
- **Bash**: Unix-based command line shell.
- **Python**: Cross-platform script engine used for custom parsing.

## 2. Automation and SOAR
- **SOAR (Security Orchestration, Automation, and Response)**: Aggregates alerts, runs automated scripts (playbooks) to contain threats, and integrates distinct security tools.
"""
    },
    "4.8": {
        "title": "Incident Response & Digital Forensics",
        "content": """# Sub-Objective 4.8: Execute Incident Response Activities

## 1. Incident Response Steps
1. **Preparation**: Training, establishing tools, writing templates.
2. **Detection & Analysis**: Evaluating alerts to confirm breaches.
3. **Containment**: Isolating affected systems to prevent spread.
4. **Eradication**: Removing malware and vulnerabilities.
5. **Recovery**: Restoring clean systems to production.
6. **Post-Incident Activity (Lessons Learned)**: Analyzing response and updating guides.

## 2. Order of Volatility
During evidence acquisition, collect data from the most volatile resources first:
1. **Registers & Cache** (CPU registers, L1/L2 cache).
2. **Routing Tables, ARP Cache, Process Table, RAM** (System memory).
3. **Temporary File Systems** (Temporary swap files).
4. **Local Disk Storage** (HDD/SSD files).
5. **Remote Logging Data / Network Backups**.

## 3. Chain of Custody
Document listing who handled physical or digital evidence, containing signatures, timestamps, and hash codes (MD5/SHA-256) to ensure integrity for legal admissibility.
"""
    },
    "4.9": {
        "title": "Analyzing Data for Security Monitoring",
        "content": """# Sub-Objective 4.9: Analyze Data for Security Monitoring

## 1. Security Logs Analysis
- **Firewall Logs**: Check for blocked outbound connections or scan patterns.
- **Web Server Logs**: Analyze HTTP response codes (e.g., 404 for scanning, 500 for SQLi errors) and User Agent fields.
- **DNS Logs**: Look for high-volume NXDOMAIN errors or queries targeting domain names associated with command-and-control (C2) servers.
"""
    },
    "5.1": {
        "title": "Security Governance & Policies",
        "content": """# Sub-Objective 5.1: Explain the Components of Security Governance

## 1. Governance Hierarchy
- **Policies**: High-level, mandatory organizational statements defined by executives.
- **Standards**: Mandatory rules, technical baselines, or settings configurations.
- **Procedures**: Compulsory, step-by-step instructions to execute tasks.

## 2. Data Roles
- **Data Owner**: Executive responsible for the overall data asset.
- **Data Controller**: Entity deciding the purpose and legal means of processing personal data.
- **Data Processor**: Entity performing data processing operations on behalf of the Controller.
- **Data Custodian**: Admin responsible for implementing security controls, backups, and encryption.
"""
    },
    "5.2": {
        "title": "Risk Management & Calculation Formulas",
        "content": """# Sub-Objective 5.2: Explain Risk Management Processes and Concepts

## 1. Quantitative Risk Analysis Formulas
- **Single Loss Expectancy (SLE)**: Cost of a single risk occurrence.
  $$\\text{SLE} = \\text{Asset Value (AV)} \\times \\text{Exposure Factor (EF)}$$
- **Annualized Loss Expectancy (ALE)**: Expected yearly cost of a risk.
  $$\\text{ALE} = \\text{Annualized Rate of Occurrence (ARO)} \\times \\text{SLE}$$

## 2. Recovery Milestones
- **Recovery Time Objective (RTO)**: Maximum acceptable duration of downtime before service restoration.
- **Recovery Point Objective (RPO)**: Maximum acceptable age of data lost during an outage (data backup age tolerance).

## 3. Risk Treatment Strategies
- **Mitigation**: Deploying controls (firewalls, training) to reduce impact/likelihood.
- **Acceptance**: Intentionally bearing the risk because control cost exceeds potential loss.
- **Avoidance**: Stopping the risk-inducing activity entirely (decommissioning a service).
- **Transfer (Sharing)**: Shifting the risk impact to a third party (cyber insurance).
"""
    },
    "5.3": {
        "title": "Third-Party Vendor Contracts",
        "content": """# Sub-Objective 5.3: Explain Third-Party Risk Assessment and Management

## 1. Vendor Agreement Frameworks
- **SLA (Service Level Agreement)**: Compulsory performance metrics and uptime commitments.
- **MOU (Memorandum of Understanding)**: Non-binding agreement mapping common intentions.
- **MOA (Memorandum of Agreement)**: Binding document describing cooperative operations.
- **SOW (Statement of Work)**: Outline of deliverables, timelines, and payment structures.
"""
    },
    "5.4": {
        "title": "Compliance and Privacy",
        "content": """# Sub-Objective 5.4: Explain Compliance and Privacy Concepts

## 1. Privacy Regulations
- **GDPR (General Data Protection Regulation)**: Strict EU framework protecting data privacy rights.
- **HIPAA (Health Insurance Portability and Accountability Act)**: Protects patient medical records.

## 2. Audits and Privacy Tools
- **PIA (Privacy Impact Assessment)**: Review to evaluate how PII is collected and protected.
- **SOC 2 Type II**: Detailed independent audit reporting security control effectiveness over time.
"""
    },
    "5.5": {
        "title": "Security Audits and Assessments",
        "content": """# Sub-Objective 5.5: Explain Audit and Assessment Processes

## 1. Auditing Classifications
- **Internal Audits**: Self-assessments performed by company staff to verify compliance and security posture prior to formal audits.
- **External Audits**: Independent reviews conducted by third-party auditors (e.g. CPA firms) to issue compliance certifications.

## 2. Audit Verification
- Collecting security logs, network designs, configuration scripts, and employee training records to prove compliance.
"""
    },
    "5.6": {
        "title": "Security Awareness and Training",
        "content": """# Sub-Objective 5.6: Explain Security Awareness and Training

## 1. Awareness Programs
- **Phishing Simulations**: Emulating fake phishing attacks to track click rates and reporting behaviors.
- **Clean Desk Policy**: Requiring locking sensitive papers and hardware away when away from workstations.
- **Training Metrics**: Evaluating training success through compliance completion rates and reduced security incidents.
"""
    }
}

for sub_code, module in modules.items():
    filepath = os.path.join(modules_dir, f"{sub_code}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(module["content"])
    print(f"Created module file: {filepath}")

print("All 28 reading modules generated successfully.")
