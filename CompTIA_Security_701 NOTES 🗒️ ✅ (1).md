# CompTIA_Security_701 NOTES 🗒️ ✅ (1)

## Page 1

🌐 🌐   CompTIA Security+ (701)

Study Notes 📑

## Page 2

Summarize Fundamental Security Concepts................................................................................. 3

Security Concepts........................................................................................................................... 3

Security Controls ............................................................................................................................ 4

Compare Threat Types ................................................................................................................... 7

Threat Actors .................................................................................................................................. 7

Attack Surfaces ............................................................................................................................... 9

Social Engineering .........................................................................................................................11

Explain Cryptographic Solutions .................................................................................................. 12

Cryptographic Algorithms ............................................................................................................. 12

Public Key Infrastructure .............................................................................................................. 13

Cryptographic Solutions ............................................................................................................... 14

Implement Identity and Access Management .............................................................................. 16

Authentication ............................................................................................................................... 16

Authorization ................................................................................................................................. 18

Identity Management .................................................................................................................... 20

Secure Enterprise Network Architecture ...................................................................................... 21

Enterprise Network Architecture ................................................................................................... 21

Network Security Appliances ........................................................................................................ 22

Secure Communications .............................................................................................................. 24

Secure Cloud Network Architecture ............................................................................................. 25

Cloud Infrastructure ...................................................................................................................... 25

Embedded Systems and Zero Trust Architecture ........................................................................ 27

Explain Resiliency and Site Security Concepts ........................................................................... 29

Asset Management ....................................................................................................................... 29

Redundancy Strategies ................................................................................................................ 31

Physical Security .......................................................................................................................... 33

Explain Vulnerability Management ............................................................................................... 34

Device and OS Vulnerabilities ...................................................................................................... 34

Application and Cloud Vulnerabilities ........................................................................................... 36

Vulnerability Identification Methods .............................................................................................. 38

Vulnerability Analysis and Remediation ....................................................................................... 39

Evaluate Network Security Capabilities ....................................................................................... 41

Network Security Baselines .......................................................................................................... 41

Network Security Capability Enhancement .................................................................................. 44

Contents

## Page 3

Definition: Protection of data resources from unauthorized access, attack,

theft, or damage.

Assess Endpoint Security Capabilities ......................................................................................... 46

Implement Endpoint Security ....................................................................................................... 46

Mobile Device Hardening ............................................................................................................. 48

Enhance Application Security Capabilities ................................................................................... 49

Application Protocol Security Baselines ....................................................................................... 49

Cloud and Web Application Security Concepts............................................................................ 51

Explain Incident Response and Monitoring Concepts ................................................................. 53

Incident Response ........................................................................................................................ 53

Digital Forensics ........................................................................................................................... 55

Data Sources ................................................................................................................................ 58

Alerting and Monitoring Tools ....................................................................................................... 59

Analyze Indicators of Malicious Activity........................................................................................ 62

Malware Attack Indicators............................................................................................................. 62

Physical and Network Attack Indicators ....................................................................................... 64

Application Attack Indicators ........................................................................................................ 66

Summarize Security Governance Concepts ................................................................................ 66

Policies, Standards, and Procedures ........................................................................................... 66

Change Management ................................................................................................................... 68

Automation and Orchestration...................................................................................................... 70

Explain Risk Management Processes.......................................................................................... 72

Risk Management Processes and Concepts ............................................................................... 72

Vendor Management Concepts .................................................................................................... 74

Audits and Assessments .............................................................................................................. 77

Summarize Data Protection and Compliance Concepts ............................................................. 78

Data Classification and Compliance ............................................................................................ 78

Personnel Policies ........................................................................................................................ 80

■

Summarize Fundamental Security Concepts

Security Concepts

● Security Concepts Study Notes:

1. Information Security:
## Page 4

2.
3.
4.
5.
CIA Triad:

■  Confidentiality: Data accessible only to authorized individuals.

■  Integrity: Data stored and transferred as intended, with authorized

modifications.

■  Availability: Information readily accessible to authorized users.

Additional Property: Non-repudiation, preventing denial of actions like

creating or modifying data.

Definition: Provisioning secure processing hardware and software.

Five Functions (NIST Framework): ■  Identify: Develop security policies, evaluate risks, recommend

controls.

■  Protect: Secure IT assets throughout the lifecycle.

■  Detect: Proactive monitoring for new threats.

■  Respond: Analyze, contain, eradicate threats.

■  Recover: Restore systems and data post-attack.

Importance: Guides control selection, aids in risk management and

compliance.

Definition: Process identifying deviations from framework requirements.

Purpose: Assess current cybersecurity capabilities, prioritize investments

for improvement.

Components: Outcome-based, identifies missing/poorly configured

controls.

Utilization: Initial adoption, compliance fulfillment, periodic validation.

Involvement: Can engage third-party consultants for complex assessments.

Definition: Governs interactions between subjects (users/devices) and

- bjects (resources).
Components:

■  Identification: Unique representation of users/devices.

■  Authentication: Proving identity, often via passwords or digital

certificates.

■  Authorization: Determining and enforcing resource access rights.

■  Accounting: Tracking authorized resource usage and detecting

unauthorized attempts.

Implementation: Often through Identity and Access Management (IAM)

systems.

AAA Framework: Alternative terminology for authentication, authorization,

and accounting.

Application of Access Control:

E-commerce Example: Enroll users, manage orders, ensure payment

integrity, record customer actions for accountability.

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

Gap Analysis:

Access Control:

Cybersecurity Framework:

## Page 5

■

■

■

■

2.
Definition: Measures to ensure information and cybersecurity assurance.

Importance: Selecting and implementing appropriate controls for different

scenarios.

Responsibility: Often falls under the purview of IT departments within

- rganizations.
Security Control Categories:

Managerial Controls: Oversight of information systems, including risk

identification and control selection.

Security Controls

● Security Controls Study Notes:

1. Introduction to Security Controls:
## Page 6

3.
4.
5.
6.
Operational Controls: Implemented by people, such as security training

programs.

Technical Controls: Implemented as hardware, software, or firmware, like

firewalls and antivirus software.

Physical Controls: Measures like alarms and security cameras to deter and

detect physical access.

Preventive Controls: Aim to eliminate or reduce the likelihood of successful

attacks.

Detective Controls: Identify and record attempted or successful intrusions

during an attack.

Corrective Controls: Reduce the impact of security policy violations after an

attack.

Additional Types:

■  Directive Controls: Enforce behavioral rules, often through policies

- r training.
■  Deterrent Controls: Discourage attackers psychologically, such as

warning signs.

■  Compensating Controls: Substitute for principal controls to provide

equivalent protection.

Information Security Roles and Responsibilities:

Chief Information Officer (CIO): Overall responsibility for IT and often

security.

Chief Security Officer (CSO) or Chief Information Security Officer (CISO):

Internal security leadership.

Managers: Departmental responsibility for security domains.

Technical and Specialist Staff: Implement, maintain, and monitor security

policies and controls.

Nontechnical Staff: Comply with policies and relevant legislation.

Skills required for IT professionals with security responsibilities, including

risk assessment, system configuration, incident response, and training.

Security Operations Center (SOC): Monitors and protects critical

information assets, typically in larger corporations.

DevSecOps: Integration of security expertise into software development

and operations processes.

Incident Response: Dedicated teams for handling security incidents, either

as part of SOC or standalone units.

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

■

Information Security Competencies:

Information Security Business Units:

Functional Types of Security Controls:

## Page 7

●  Threat Actors Study Notes:

Introduction to Vulnerability, Threat, and Risk:

●  Vulnerability: Weakness in security systems that can be exploited.

●  Threat: Potential for exploitation by a threat actor, intentional or

unintentional.

●  Risk: Level of hazard posed by vulnerabilities and threats, calculated

based on likelihood and impact.

Compare Threat Types

Threat Actors

## Page 8

Attributes of Threat Actors:

●  Internal/External: Degree of access before initiating an attack, either

unauthorized (external) or authorized (internal/insider).

●  Level of Sophistication/Capability: Ability to use advanced exploit

techniques and tools.

●  Resources/Funding: Support necessary for sophisticated threat actors,

- ften from nation-states or organized crime.
●  Motivations: Reasons for perpetrating attacks, including financial gain,

political agendas, or revenge.

Threat Actor Types:

●  Hackers:

●  Unauthorized (black hat) or authorized (white hat), with varying levels of

skill.

●  Increasingly work in teams or groups, known as hacktivist groups, to

promote political agendas.

●  Nation-State Actors:

●  Often pursue espionage and disinformation for strategic advantage, with

plausible deniability.

●  Known for sophisticated attacks, such as advanced persistent threats

(APTs).

●  Organized Crime and Competitors:

●  Focus on financial fraud, blackmail, and extortion, operating across

jurisdictions.

●  Competitors may engage in cyber espionage for theft or disruption.

●  Internal Threat Actors:

●  Can be permanent insiders (employees) or temporary insiders

(contractors, guests).

●  Motivated by revenge, financial gain, or unintentional actions like poor

security practices.

●  Whistleblowers may release information ethically, while unintentional

threats arise from lack of awareness or shadow IT.

Motivations and Strategies of Threat Actors:

●  Strategies include service disruption, data exfiltration, and disinformation,

affecting confidentiality, integrity, and availability.

●  Motivations range from chaotic (e.g., causing chaos) to financial (e.g.,

fraud, extortion) and political (e.g., promoting change or furthering war

aims).

●  Threat sources and motivations evolve over time, with shifts from

- pportunistic to structured attacks associated with organized crime and
nation-states.

## Page 9

●

●

○

○

○

○

:

The attack surface refers to all points where a malicious actor could exploit a

vulnerability.

It includes network ports, applications, computers, and user interactions.

Minimizing the attack surface involves restricting access to known endpoints,

protocols, and services.

Assessment should cover the overall organization as well as specific scopes like

servers, web applications, or user identities.

:

Attack Surfaces

Assessing the Attack Surface

Attack Surface and Threat Vectors

## Page 10

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Organizations should evaluate the attributes of threat actors posing the most risk.

External threat actors have a smaller attack surface compared to insider

threats.

Threat vectors represent paths used by threat actors to execute attacks like data

exfiltration or service disruption.

Sophisticated actors plan multistage campaigns and may develop novel vectors.

:

Vulnerabilities in software allow threat actors to exploit flaws in code or design.

Patch management is crucial, as almost no software is free from vulnerabilities.

Consolidating to fewer products and ensuring consistent versions help reduce the

attack surface.

:

Unsupported systems lack vendor updates and patches, making them highly

vulnerable.

Isolating such systems reduces the likelihood of exploitation.

:

Scanning software helps identify vulnerabilities, but threat actors can also use it

for reconnaissance.

Scans can be client-based, requiring installation, or agentless, scanning without

installation.

:

Vulnerable software allows threat actors to execute code remotely or locally.

Remote exploits occur over a network, while local exploits require authenticated

access.

Securing networks involves ensuring confidentiality, integrity, and availability.

:

Lures, like malicious files, trick users into facilitating attacks.

Common lures include removable devices, executable files, document files, and

image files.

:

Threat actors use messaging systems like email, SMS, IM, web, and social

media to deliver malicious files.

Social engineering techniques persuade users to open attachments or links.

:

Threat actors target supply chains to infiltrate organizations indirectly.

Procurement management ensures reliable sources of equipment and software.

Establishing a trusted supply chain involves vetting suppliers, vendors, and

partners.

Network Vectors

Lure-Based Vectors

Message-Based Vectors

Supply Chain Attack Surface

Vulnerable Software Vectors

Client-Based versus Agentless Scanning

Unsupported Systems and Applications

## Page 11

●

●

○

○

○

:

People within organizations are part of the attack surface and are collectively

referred to as the human vector.

Social engineering exploits human psychology to manipulate individuals into

divulging information or performing actions for threat actors.

:

Employees and contractors possess valuable information about networks and

security systems, making them potential targets.

Social Engineering

Human Vectors

Social Engineering Overview

## Page 12

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

:

Cryptography ensures information security by encoding data.

Terms: Plaintext (unencrypted), Ciphertext (encrypted), Algorithm

(encryption/decryption process), Cryptanalysis (cracking cryptographic systems).

Actors: Alice (sender), Bob (recipient), Mallory (malicious attacker).

:

Uses a single secret key for both encryption and decryption.

Social engineering involves eliciting information or actions from individuals, also

known as "hacking the human."

Examples include tricking users into providing passwords, obtaining sensitive

information from help desks, or infiltrating buildings during emergencies.

:

Impersonation involves pretending to be someone else to gain trust.

Threat actors use persuasive or coercive approaches to deceive targets.

Pretexting involves crafting convincing stories to charm or intimidate targets, often

relying on privileged information about the organization.

:

Phishing combines social engineering with spoofing to trick targets into

interacting with malicious resources.

Phishing emails or messages persuade users to perform actions like installing

malware or revealing credentials.

Pharming redirects users from legitimate websites to malicious ones by corrupting

name resolution processes.

:

Typosquatting involves registering domain names similar to legitimate ones to

deceive users.

Business Email Compromise targets specific individuals within companies, often

executives, using sophisticated techniques to deceive and manipulate.

:

Brand impersonation involves accurately duplicating company logos and

formatting to create visually compelling fakes.

Disinformation aims to deceive, while misinformation involves repeating false

claims unintentionally.

:

This attack targets a group of users who frequent an unsecure third-party

website, allowing threat actors to compromise their systems through exploit code.

Watering Hole Attack

Symmetric Encryption

Phishing and Pharming

Impersonation and Pretexting

Brand Impersonation and Disinformation

Typosquatting and Business Email Compromise

Explain Cryptographic Solutions

Cryptographic Algorithms

●  Cryptographic Concepts

## Page 13

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Root CA directly issues certificates to users and computers.

Often used on private networks.

Vulnerable because if compromised, the entire PKI collapses.

Operate on a hierarchical model.

Root CA issues certificates to intermediate CAs, which in turn issue certificates to

end entities.

Provides clear certificate policies and certification path (chain of trust).

Used when PKI management is too difficult or expensive.

Deployed on machines, web servers, or program code.

Often marked as untrusted by operating systems or browsers.

Examples: Substitution and transposition algorithms.

Key exchange challenge: securely sharing the key.

Fast and efficient for bulk encryption but vulnerable if the key is intercepted.

:

Longer keys increase security by expanding the keyspace.

Example: AES-128 vs AES-256, where AES-256 has a significantly larger

keyspace.

Brute force cryptanalysis: attempting decryption with every possible key value.

:

Uses different but related public and private keys for encryption and decryption.

Public key can be freely distributed, while the private key must be kept secret.

Involves more computing overhead compared to symmetric encryption.

:

Produces fixed-length digest from plaintext, used for integrity verification.

Example: Comparing password hashes or verifying file integrity after download.

Algorithms: SHA256 (strong) and MD5 (less secure but still used for compatibility).

:

Combines public key cryptography with hashing for authentication, integrity, and

non-repudiation.

Sender creates a hash of the message and signs it with their private key.

Recipient verifies the signature using sender's public key.

:

PKCS#1 defines RSA algorithm for digital signatures.

DSA and ECDSA are used for digital signatures and were developed as part of

FIPS.

Hashing

Standards

Key Length

Third-party CAs:

Single CA Model:

Digital Signatures

Asymmetric Encryption

Self-signed Certificates:

Public Key Infrastructure

## Page 14

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

1.
2.
3.
4.
○  Cryptographic solutions are essential for implementing security controls.

○  They ensure confidentiality, integrity, and authenticity of data. ○

Used to secure data at rest, in transit, and in use.

○  Encryption renders data unreadable to unauthorized parties.

○  Protects data even if storage media is stolen or data is intercepted. ○

Data states: at rest, in transit, in use.

Bulk encryption (symmetric cipher) used for large data volumes (e.g., AES).

Asymmetric encryption (RSA, ECC) less efficient for bulk encryption.

Hybrid approach: symmetric for data encryption, asymmetric for key exchange.

Full-disk encryption (FDE) encrypts entire storage device, including metadata.

Self-encrypting drives (SEDs) have built-in encryption.

Suitable for non-critical environments like development or testing.

Process for requesting certificates.

Subject generates a key pair and submits a CSR to the CA.

CA reviews and validates the information before issuing the certificate.

Private key is not part of the CSR and must be securely stored by the subject.

CN attribute deprecated; SAN extension field used to represent identifiers.

SAN field more secure for representing FQDNs and IP addresses.

It's safer to duplicate FQDN information in CN for compatibility.

Certificates can be revoked or suspended by owner or CA for various reasons.

Revoked certificates are no longer valid; suspended certificates can be reenabled.

CA maintains a Certificate Revocation List (CRL) accessible to verify certificate

status.

Lifecycle stages: generation, storage, revocation, expiration/renewal.

Decentralized vs. centralized key management models.

Cryptoprocessors offer more secure key generation and storage.

Trusted Platform Module (TPM) and Hardware Security Modules (HSM) examples.

Archiving keys with third-party providers.

Mitigates risk of key loss or damage.

M of N controls ensure multiple authorizations for key operations.

Key Escrow:

Key Management:

Certificate Revocation:

Disk and File Encryption:

Subject Name Attributes:

Encryption for Confidentiality:

Certificate Signing Requests (CSR):

Importance of Cryptographic Solutions:

Bulk Encryption vs. Asymmetric Encryption:

Cryptographic Solutions

## Page 15

5.
6.
7.
8.
9.
10.
11.
○  Partition-based encryption allows selective encryption for different partitions.

○  Volume encryption secures entire storage resource, implemented in software.

○  File encryption encrypts individual files or folders (e.g., Microsoft's EFS).

○  Encryption at database level (TDE) protects entire database.

○  Record/column-level encryption provides granular protection.

○  Enables separation of duties between administrators and data owners.

○  Secures data in motion using protocols like TLS, IPsec, WPA.

○  Key exchange enables secure sharing of symmetric session keys.

○  Integrity and authenticity ensured through HMAC or authenticated encryption.

○  Uses Diffie-Hellman key agreement to generate session keys.

○  Ensures future compromise of server doesn't compromise past sessions. ○

Increases complexity for attackers, enhances security.

Salting prevents precomputed hash attacks by adding random value to

passwords.

Key stretching (PBKDF2) increases key length through multiple iterations.

Mitigates low-entropy password vulnerabilities.

Blockchain secures transaction records through cryptographic hashing.

Decentralized, distributed ledger ensures transparency and integrity.

Applications in finance, contracts, voting, identity management, and more.

Obfuscation hides data to make it difficult to find.

Uses include steganography, data masking, and tokenization.

Protects privacy and enhances security in certain contexts.

○

○

○

○

○

○

○

○

○

Blockchain:

Obfuscation:

Database Encryption:

Salting and Key Stretching:

Volume and File Encryption:

Perfect Forward Secrecy (PFS):

Transport Encryption and Key Exchange:

## Page 16

●

●

○

○

○

○

○

Personal Identification Number (PIN) is a form of something you know.

Modern PINs are not limited to numeric sequences and can be of any length and

character combination.

They are valid for authenticating to a single device only.

Improper credential management is a major vector for network attacks.

Password best practices policy should instruct users on choosing and maintaining

passwords.

Implement Identity and Access Management

Authentication

Password Concepts:

Windows Sign-In Screen:

## Page 17

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Credential management policy should cover various authentication methods and

educate users on social engineering attacks.

Password Length: Enforces minimum and possibly maximum length for

passwords.

Password Complexity: Requires a combination of uppercase/lowercase

alphanumeric and non-alphanumeric characters.

Password Age: Forces users to select a new password after a set number of days.

Password Reuse and History: Prevents the selection of previously used

passwords.

Aging allows logging in with the old password after a defined period but

mandates choosing a new password immediately.

Expiration disables logging in with the outdated password and effectively disables

the account.

Users often use poor credential management practices, such as reusing

passwords across multiple sites.

Password managers generate random passwords and securely store them,

reducing the risk of data breaches.

Risks include compromise of the master password or vendor's cloud storage, and

impersonation attacks.

Combines multiple authentication factors for stronger security.

Factors include something you have (like a smart card), something you are

(biometrics), and somewhere you are (location-based).

Involves physiological or behavioral identifiers like fingerprints or facial scans.

Enrollment includes acquiring a biometric sample and creating a template for

comparison.

Metrics include False Rejection Rate (FRR), False Acceptance Rate (FAR), and

Crossover Error Rate (CER).

Generated within a secure cryptoprocessor, avoiding transmission of the token.

Types include Certificate-Based Authentication, One-Time Password (OTP), and

FIDO Universal 2nd Factor (U2F).

One-time passwords sent via SMS, email, or authenticator apps.

Vulnerable to interception, with authenticator apps offering higher security than

SMS or email.

Entirely eliminates knowledge-based factors like passwords.

Relies on factors like biometrics or hardware tokens.

Password Policies:

Password Managers:

Biometric Authentication:

Soft Authentication Tokens:

Hard Authentication Tokens:

Passwordless Authentication:

Password Aging and Expiration:

Multifactor Authentication (MFA):

## Page 18

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

Utilizes FIDO2 with WebAuthn specifications for secure authentication without

passwords.

:

Authorization is a crucial aspect of identity and access management (IAM).

It involves assigning privileges to network users and services to manage access to

resources effectively.

:

DAC prioritizes the resource owner's authority.

Owners have full control over resources and can modify access control lists

(ACLs) to grant rights to others.

Widely used but vulnerable to insider threats and abuse of compromised accounts.

:

Based on security clearance levels rather than individual ownership.

Each object is assigned a classification label, and each subject is granted a

clearance level.

Subjects can access objects classified at their own level or below, ensuring

confidentiality.

:

Defines permissions based on user roles.

Each principal is assigned to one or more roles, and permissions are managed by

system owners.

Offers flexibility and scalability in permission management.

:

Authorization

● Authorization Overview

Mandatory Access Control (MAC)

Role-Based Access Control (RBAC)

Discretionary Access Control (DAC)

Attribute-Based Access Control (ABAC)

## Page 19

●

●

●

●

●

○  Utilizes subject and object attributes for access decisions.

○  Factors like location, device status, and user behavior influence access control. ○

Provides fine-grained control over access based on contextual information.

:

○  Access control policies are enforced by system rules rather than user discretion.

○  Examples include RBAC, ABAC, and MAC.

○  Conditional access systems monitor behavior and enforce access rules

dynamically.

:

○  Grants the minimum necessary privileges to perform authorized tasks.

○  Reduces the risk of compromised accounts and limits potential

damage. ○  Requires careful analysis of business workflows to determine

necessary permissions.

:

○  Involves setting up user accounts according to standardized procedures.

○  Includes identity proofing, credential issuance, hardware/software allocation, and

policy awareness training.

:

○  Location-based and time-based policies restrict account access.

○  Policies enforce authorized login hours, session durations, and geographical

constraints.

○  Privileged Access Management (PAM) controls and monitors privileged account

usage to prevent compromise.

:

○  Elevates privileges only when needed for a limited duration.

○  Ensures zero standing privileges (ZSP) to minimize attack surface.

○  Implemented through temporary elevation, password vaulting, or ephemeral

credentials.

Least Privilege Principle

Rule-Based Access Control

User Account Provisioning

Just-in-Time (JIT) Permissions

Account Restrictions and Policies

## Page 20

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Identity Management Exam Objectives:

Implementing and maintaining identity and access management.

Authentication Provider:

Essential feature of an OS for user authentication.

Relies on cryptographic hashes for knowledge-based authentication.

Windows Authentication:

Local sign-in: LSASS compares credentials to hash in SAM database.

Network sign-in: LSASS authenticates via Active Directory using Kerberos or

NTLM.

Remote sign-in: Authentication over VPN, enterprise Wi-Fi, or web portal.

Linux Authentication:

Local user account info in /etc/passwd, password hash in /etc/shadow.

Network login via SSH; can use cryptographic keys.

Pluggable Authentication Module (PAM) enables different authentication

methods.

Directory Services:

Store info about users, computers, security groups, etc.

LDAP is a common protocol for interoperability.

Distinguished Name (DN) uniquely identifies resources in a directory.

Single Sign-on (SSO):

Authenticates once, access multiple services without re-entering credentials.

Identity Management

## Page 21

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Kerberos is a common SSO protocol, authenticates users and services.

Federation:

Extends network access to partners, suppliers, customers.

Trusts external networks for authentication and authorization.

SAML (Security Assertion Markup Language):

Protocol for exchanging authentication and authorization data.

Uses XML for assertions, HTTP/HTTPS for communication.

OAuth (Open Authorization):

Protocol for sharing user attributes between sites.

Allows linking identity to consumer sites without sharing passwords.

Uses JSON Web Tokens (JWTs) for claims data, supports various grant type

Network Addressing:

IPv4 addresses use a /24 prefix to define a subnet, written as 255.255.255.0.

IPv6 addresses are 128-bit and hierarchical, with the last 64 bits representing the

host's interface ID.

Logical Addressing and Access Control:

Hierarchical network architecture assigns separate IP subnets to access blocks,

facilitating access control.

Each access block is allocated a subnet, ensuring logical separation (e.g., guest

network vs. enterprise LAN).

VLANs (Virtual LANs):

VLANs segment networks into separate broadcast domains.

VLAN IDs (2 to 4,094) are assigned to switches, enabling different ports on the

same switch to belong to different VLANs.

Security Zones:

Internal security topology based on network segmentation and access control.

Different zones for different levels of trust and access control requirements.

Attack Surface:

Points of vulnerability at different network layers (1/2, 3, 4/7).

External and internal attack surfaces require different security controls.

Port Security:

Measures to control physical access to network ports.

Methods include MAC filtering, MAC limiting, and IEEE 802.1X authentication.

Secure Enterprise Network Architecture

Enterprise Network Architecture

## Page 22

●

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Physical Isolation:

Critical hosts isolated from networks for security.

Challenges include management and restricted access.

Architecture Considerations:

Factors include costs, scalability, availability, resilience, power usage, patch

availability, and risk transference.

:

Stateless firewall: Does not preserve information about network sessions.

Analyzes each packet independently without record of previous packets.

Vulnerable to attacks spread over multiple packets.

Can introduce traffic flow problems, especially with load balancing or dynamically

assigned ports.

:

Tracks information about established sessions between hosts.

Incorporates stateful inspection capability, storing session data in a state table.

Checks incoming packets against existing connections in the state table.

Once a connection is allowed, traffic usually passes unmonitored to conserve

processing effort.

Can occur at layer 4 and layer 7.

:

Examines the TCP three-way handshake to distinguish new from established

connections.

Tracks legitimate TCP connections following SYN > SYN/ACK > ACK sequence.

Can detect anomalies like SYN without ACK or sequence number anomalies.

Capable of tracking UDP traffic and detecting IP header and ICMP anomalies.

:

Inspects headers and payload of application-layer packets.

Verifies application protocol matches the port to prevent malicious data transfer.

Can analyze HTTP headers and webpage formatting code to identify threats.

Also known as application-aware firewalls or deep packet inspection.

:

Perform application layer filtering and operate on a store-and-forward model.

Network Security Appliances

●  Packet Filtering Firewall

Proxy Servers

Layer 4 Firewall

Layer 7 Firewall

Stateful Inspection Firewall

## Page 23

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Deconstruct packets, perform analysis, and rebuild packets according to rules.

Can be non-transparent (client must be configured) or transparent (intercepts

traffic without client reconfiguration).

:

Provide outbound traffic filtering and enable client connections to external

resources like websites.

Offer traffic management, security, and caching benefits.

:

Provide inbound traffic filtering and are typically deployed on the network edge.

Listen for client requests from the public network, filter, and forward requests to

application servers.

:

Perform real-time analysis of network traffic or system/application logs.

Utilize sensors to capture traffic data, which is then analyzed by IDS software.

Raise alerts or generate log entries for detected threats but do not actively block

traffic.

:

Capable of active response to detected threats, including blocking noncompliant

traffic, resetting connections, or redirecting traffic for further analysis.

:

NGFW incorporates intrusion detection functionalities into firewall systems.

UTM centralizes various security controls into a single appliance for

comprehensive security management.

:

Distribute client requests across server nodes to optimize resource usage,

provide fault tolerance, and mitigate denial of service attacks.

Can be Layer 4 (IP and port-based) or Layer 7 (application-aware) load balancers.

Employ scheduling algorithms and health checks to manage traffic distribution

effectively.

:

Designed to protect web servers and back-end databases from code injection

and denial of service attacks.

Use application-aware processing rules and pattern matching to filter traffic and

detect threats.

Can be deployed as appliances or plug-in software for web server platforms.

Load Balancers

Reverse Proxy Servers

Forward Proxy Servers

Web Application Firewalls (WAF)

Intrusion Detection Systems (IDS)

Intrusion Prevention Systems (IPS)

Next-Generation Firewalls (NGFW) and Unified Threat Management (UTM)

## Page 24

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

:

Remote Access VPN: Initiated by the client.

Site-to-Site VPN: Configured to operate automatically, connecting two or more

private networks.

Host-to-Host Tunnel: Securing traffic between two computers on an untrusted

private network.

:

Legacy Protocols: Deprecated due to inadequate security (e.g., PPTP).

Modern Protocols: TLS and IPsec preferred for VPN access.

:

Mutual authentication using digital certificates.

TLS creates an encrypted tunnel for user authentication and data transmission.

:

Operates at OSI layer 3 (network layer).

Core Protocols: Authentication Header (AH) and Encapsulating Security Payload

(ESP).

Modes: Transport mode for host-to-host, tunnel mode for site-to-site VPNs.

:

Establishes security associations (SA) for IPsec.

Negotiations in two phases for key agreement and cipher selection.

:

Remote access to private networks via secure tunnel over public networks.

Includes graphical and terminal server access methods.

Secure Communications

VPN Protocols

VPN Topologies

Remote Desktop

Internet Key Exchange (IKE)

Transport Layer Security (TLS) Tunneling

Internet Protocol Security (IPsec) Tunneling

## Page 25

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Enforces resource separation at the operating system level.

Defines isolated "cells" for each user instance to run in.

Allocated CPU and memory resources for each container.

Processes run through the native OS kernel.

Containers may run slightly different OS distributions.

Docker is a well-known container virtualization product.

Supports microservices and serverless architecture.

Used in implementing corporate workspaces on mobile devices.

Cloud provider manages infrastructure and allocates resources automatically.

Charges only for actual usage of the application.

Examples include chatbots, mobile backends, IoT services.

Major providers include AWS, Microsoft Azure, Google Cloud.

Provides scalable, cost-effective infrastructure for event-driven tasks.

Collection of small, independent services focusing on specific business

capabilities.

Modular design with well-defined interfaces.

Allows efficient development and deployment of complex applications.

Enables teams to work independently on different features.

Promises agility, scalability, and resilience.

Risks include integration issues and complexity.

Manages computing infrastructure using machine-readable definition files.

YAML, JSON, and HCL formats are common.

Automates deployment and management of infrastructure.

Ensures consistency and repeatability across environments.

Examples: Microsoft's Remote Desktop Protocol (RDP), TeamViewer, Virtual

Network Computing (VNC).

:

Provides secure remote access to command line terminal.

Authentication methods: Username/password, public key, Kerberos.

:

OOB management ensures separate network for administrative access.

Jump servers provide controlled access to administrative interfaces on hosts in

secure zones.

Enhances security by limiting direct access to administrative interfaces.

Microservices:

Secure Shell (SSH)

Serverless Computing:

Infrastructure as Code (IaC):

Out-of-Band Management and Jump Servers

Secure Cloud Network Architecture

Cloud Infrastructure

●  Containerization:

## Page 26

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Implemented using tools like Terraform.

Load balancing distributes network traffic to improve performance and

availability.

Edge computing optimizes processing location for reduced latency.

Auto-scaling adjusts resources based on demand dynamically.

Abstract model divides network functions into control, data, and management

planes.

SDN applications define policy decisions on the control plane.

Implemented through APIs interfacing with network devices.

Manages both physical and virtual network appliances.

Supports rapid deployment of virtual networking using NFV.

Data replication, redundancy, and auto-scaling ensure high availability.

Disaster recovery, SLAs, and ISAs are critical for data protection.

Power efficiency, compute capabilities, and ease of deployment enhance cloud

infrastructure.

Data protection, patch management, and secure communication are essential.

SD-WAN and SASE provide enhanced security features for cloud environments.

Zero trust security model and IAM are crucial for secure access.

Cloud Architecture Features:

Cloud Security Considerations:

Software Defined Networking (SDN):

Load Balancing, Edge Computing, Auto-Scaling:

## Page 27

●

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

:

SCADA replaces control servers in large-scale ICSs.

Typically runs as software on ordinary computers.

Gathers data from and manages plant devices with embedded PLCs (field

devices).

Uses WAN communications like cellular or satellite to link to field devices.

:

Used in energy (power generation, distribution), industrial (mining, refining),

fabrication/manufacturing, logistics, and facilities management.

Historically built without strong IT security, but awareness of security importance is

increasing.

:

Vulnerable to cyberattacks.

Example: Stuxnet worm targeting Iran's nuclear program.

NIST Special Publication 800-82 provides security control recommendations.

:

Safety is paramount.

Prioritize availability and integrity over confidentiality (AIC triad instead of CIA

triad).

:

Critical for sectors like energy, manufacturing, transportation, and water

treatment.

Robust cybersecurity measures like network segmentation, access controls,

intrusion detection, and encryption are essential.

:

Refers to networked physical devices with sensors and connectivity.

Used in various sectors like smart homes, smart cities, healthcare, agriculture, etc.

Factors driving adoption include decreased sensor costs, advances in connectivity

tech, and the COVID-19 pandemic.

:

Many devices lack adequate security measures.

Standardization issues make security implementation challenging.

Large volume of data increases the risk of breaches and cyberattacks.

:

Recommendations from organizations like IoTSF, IIC, CSA, and ETSI.

:

Assumes nothing is trusted by default.

Embedded Systems and Zero Trust Architecture

SCADA Overview

Internet of Things (IoT)

Applications of ICS/SCADA

Cybersecurity in ICS/SCADA

Best Practices for IoT Security

Zero Trust Architecture (ZTA)

Priorities in Industrial Systems

Security Concerns in ICS/SCADA

Security Risks Associated with IoT

## Page 28

●

●

●

●

●

○

○

○

○

○

○

○

○

Requires continuous authentication and verification for all users, devices, and

applications.

NIST SP 800-207 defines ZTA and CISA provides a maturity model.

:

Shifts focus from defending network boundaries to protecting individual

resources.

Essential due to trends like cloud adoption, remote work, mobile devices,

- utsourcing, and wireless networks.
:

Network and endpoint security, IAM, policy-based enforcement, cloud security,

network visibility, network segmentation, data protection, and threat

detection/prevention.

:

Adaptive identity, threat scope reduction, policy-driven access control, and device

posture assessment.

:

Control plane manages policies, while data plane establishes secure sessions. ○

Separation allows for flexibility and scalability.

:

Google BeyondCorp, DoD’s JEDI cloud, Cisco Zero Trust Architecture, Palo Alto

Networks Prisma Access.

Deperimeterization

Zero Trust Security Concepts

Zero Trust Architecture Examples

Key Components of Zero Trust Architecture

Control and Data Planes in Zero Trust Models

## Page 29

Manual Inventory: Feasible for smaller organizations or specific asset types, involves

physically inspecting assets and recording relevant information.

Network Scanning: Tools like Nmap, Nessus, or OpenVAS automatically discover and

enumerate networked devices, including open ports and services.

Asset Management Software: Solutions like Lansweeper or ManageEngine

automatically discover, track, and catalog various assets, providing a centralized

dashboard for management.

Configuration Management Database (CMDB): Centralized repository for IT

infrastructure information, managed by tools like ServiceNow or BMC Remedy.

Mobile Device Management (MDM) Solutions: Manage mobile assets like smartphones

and tablets using solutions like Microsoft Intune or VMware Workspace ONE.

Cloud Asset Discovery: Cloud-native or third-party tools like AWS Config or CloudAware

help discover and catalog assets deployed in the cloud.

●  Inventory and enumeration tasks involve creating and maintaining a comprehensive list

- f all assets within an organization, including hardware, software, data, and network
equipment.

●  Regularly updating and verifying asset inventory helps organizations manage assets

effectively and ensures accurate information about each asset's location, owner, and

status.

●  Asset monitoring includes tracking performance, security, and usage to detect potential

issues, vulnerabilities, or unauthorized access promptly.

●  Proactive asset monitoring helps mitigate risks, optimize resource utilization, and ensure

compliance with regulatory requirements.

Select hardware and software solutions with strong security features, prioritize reputable

vendors providing ongoing support.

Integrate solutions seamlessly with existing security infrastructure like firewalls, intrusion

detection systems, or SIEM platforms.

Assess total cost of ownership (TCO) considering initial purchase price, ongoing costs,

and potential security incidents.

Prioritize cybersecurity during acquisition to reduce breach risk, enhance compliance,

and protect critical data and systems.

●

●

●

●

●

●

●

●

●

●

Explain Resiliency and Site Security Concepts

Asset Management

Asset Protection Concepts:

Monitoring and Asset Tracking:

Asset Acquisition/Procurement:

Ways to Perform Asset Enumeration:

## Page 30

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Adds an extra layer of protection against unauthorized access or theft.

Ensures compliance with regulations regarding sensitive data protection.

Essential for safeguarding sensitive customer data, intellectual property, or trade

secrets.

Snapshots capture system state at a specific time, useful for VMs, filesystems, and

SANs.

Replication creates redundant copies of data for availability and recovery.

Journaling tracks changes to data for recovery and consistency, useful for filesystems.

Advanced techniques like remote journaling, SAN replication, and VM replication

enhance data protection across multiple locations and systems.

Essential for ensuring availability and integrity of critical data and systems.

Regularly test and verify backup data to ensure reliability of recovery process.

Enterprise backup solutions offer scalability, performance, advanced features like data

encryption and ransomware protection, and integration with various environments.

Assets include critical resources, information, and infrastructure components that must

be protected from threats and unauthorized access.

Identify and prioritize assets based on sensitivity and potential impact on core functions

if breached.

Use standard naming conventions and configuration management to ensure consistency

and manageability.

Implement ITIL framework elements for effective configuration management.

Sanitization and destruction processes remove sensitive information from storage media

to prevent unauthorized access.

Certification provides verification of data destruction process compliance with industry

standards and regulations.

Active methods like overwriting or physical destruction ensure irrecoverability of data

from storage devices.

Proper disposal of assets at the end of lifecycle or when no longer needed minimizes

security risks and ensures compliance.

Data Backups:

Encrypting Backups:

Snapshot, Replication, and Journaling:

Secure Data Destruction and Asset Disposal:

## Page 31

●

●

○

○

○

○

○

○

○

: Site-level resiliency is common in enterprise

environments.

: Provides similar service levels and can be always

available.

: Used in emergencies, might take longer to set up.

: Technique ensuring redundancy, quickly taking over functionality from a

failed asset.

:

■  Hot Site: Immediate failover, fully operational and updated.

■  Warm Site: Similar to hot site but requires loading latest data set.

■  Cold Site: Longer setup time, may be empty building with lease agreement.

: Distributing recovery sites across different locations to

minimize regional disaster impact.

: Cloud providers offer affordable redundancy due to economies of

scale.

: Cloud services allow redundant capabilities without overprovisioning.

: Enables quick setup and deployment of redundant systems.

: Cloud providers offer tools to reduce redundant

infrastructure complexity.

: Cloud providers invest heavily in security

and compliance.

: Validates system performance under expected or peak loads.

: Validates seamless transition between primary and secondary

infrastructure.

Redundancy Strategies

● Site Considerations

Resiliency Provisioning

Alternate Processing Site

Recovery Site

Failover

Site Resiliency Levels

○ Geographic Dispersion

Cloud as Disaster Recovery (DR)

○ Cost Efficiency

○ Scalability

○ Faster Deployment

○ Simplified Management

○ Improved Security and Compliance

Testing Redundancy and High Availability

Load Testing

Failover Testing

## Page 32

●

●

●

●

●

●

●

●

●

○

○

○

○

○

: Validates effective detection and response to

failures and performance issues.

: Load balancing distributes traffic, while

clustering allows redundant processing nodes to accept connections.

: Active/passive ensures no

performance impact during failover, while active/active utilizes maximum capacity

but may degrade performance during failover.

: Provide redundancy, can be replaced without system

shutdown.

: Support remote power monitoring

and integrate with UPSs.

: Provide temporary power source during outages.

: Provide backup power for extended periods.

: Reduces risk by using multiple technologies and platforms.

: Implements multiple layers of protection against cyber threats.

: Reduces single point of failure and promotes healthy

competition.

: Mitigates risk associated with vendor lock-in and

disruptions.

: Encourages innovation and ensures better value

for investments.

Multi-Cloud Strategies

: Diversifies risk, improves security posture, and

promotes vendor independence.

: Enhances flexibility, agility, and cost efficiency.

: Cybersecurity tools to

detect and defend against attacks by diverting attackers' attention and gathering

intelligence.

: Uses tactics like bogus DNS entries, web server decoys, and

fake telemetry to raise attack cost and tie up adversary's resources.

: Tabletop exercises, failover tests, simulations, and parallel

processing tests.

: Identifies vulnerabilities, evaluates recovery strategies,

and improves preparedness for real-life incidents.

Disruption Strategies

○ Active Defense

Testing Resiliency

○  Method of Testing

○  Importance of Testing

Documentation

○

Monitoring Systems Testing

Clustering

Load Balancing vs. Clustering

Active/Passive vs. Active/Active Clustering

Power Redundancy

○  Dual Power Supplies

○  Managed Power Distribution Units (PDUs)

○  Battery Backups and UPSs

○  Generators

Diversity and Defense in Depth

○  Platform Diversity

○  Defense in Depth

Vendor Diversity

○ Cybersecurity Benefits

○  Business Resilience

○  Innovation and Competition

Cybersecurity Benefits

Business Benefits

Deception Technologies

Honeypots, Honeynets, Honeyfiles, and Honeytokens

## Page 33

1.
2.
3.
4.
5.
6.
Business Continuity Documentation: Covers planning, implementation, and

evaluation.

Test Plans, Scripts, and Results: Provide structure for testing process and

communication with stakeholders.

Third-Party Assessments and Certifications: Offer objective evaluation,

compliance verification, and recommendations for improvement.

○  Physical security is integral to cybersecurity, protecting physical assets like

servers and data centers.

○  Measures include access control, surveillance, and environmental controls.

○  Effective physical security reduces the risk of unauthorized access and insider

threats.

○  Access control mechanisms include biometric scanners, smart cards, and key

fobs.

○  Surveillance systems involve video cameras, motion sensors, and alarms.

○  Environmental controls like backup power and fire suppression are crucial for data

centers.

Zone Implementation:○  Zones use barriers and security mechanisms to control entry and exit points.

○  Each zone should have increasingly restrictive access.

○  Entry points to secure zones should be discreet to prevent inspection by intruders.

○  Enhances security using non-obvious features in physical spaces. ○  Promotes

safety and deters criminal activity in various settings.

○  Barricades channel people through defined entry and exit points.

○  Security fencing needs to be transparent, robust, and secure against climbing. ○

Security lighting improves safety and acts as a deterrent at night.

○

○

○

Physical Security Controls:

Fundamental Security Concepts:

Bollards and Existing Structures:

Barricades, Fencing, and Lighting:

Physical Security through Environmental Design:

Physical Security

## Page 34

7.
8.
2.
3.
Bollards prevent vehicular access to restricted areas.

Existing structures can be adjusted for improved site layout and security.

Gateways require secure locks, which can be physical, electronic, or biometric.

Access control vestibules regulate entry to secure areas, preventing tailgating.

Access badges replace physical keys and provide access through card readers.

Surveillance enhances resilience, with guards providing visual deterrence. ○

Cameras offer cost-effective monitoring and can use AI for smart security.

Alarms supplement other security controls, detecting and deterring threats effectively.

○  Android and iOS are primary computing platforms, prone to attacks.

○  Android's open-source nature leads to similar benefits and problems as Linux.

○  Fragmentation among manufacturers and versions of Android results in

inconsistent patching.

○  iOS, though not open source, faces significant vulnerabilities.

○  Microsoft Windows: MS08-067 and MS17-010 allowed remote code execution,

exploited by Conficker and WannaCry.

○  macOS: "Shellshock" vulnerability in Unix-based systems.

○  Android: "Stagefright" vulnerability allowed remote code execution via MMS.

○  iOS: Google's Project Zero discovered vulnerabilities used in "watering hole"

attacks.

○  Linux: "Heartbleed" bug compromised OpenSSL cryptographic software.

○  EOL systems lack vendor support and critical security patches, posing

vulnerabilities.

○  Legacy systems are outdated but may still receive support. ○

Notable examples include Windows 7 and Server 2008.

○

○

○

○

○

○

○

1. Mobile OS Vulnerabilities:
Example OS Vulnerabilities:

Security Guards and Cameras:

Legacy and End-of-Life Systems:

Gateways, Locks, and Access Control:

Explain Vulnerability Management

Device and OS Vulnerabilities

## Page 35

●

●

○

○  Meltdown and Spectre vulnerabilities impacted computers and mobile devices.

○  "LoJax" exploited UEFI firmware.

EOL hardware vulnerabilities arise from discontinued updates.

○  VM escape allows attackers to access host systems.

○  Examples include "Cloudburst" vulnerability in VMware.

○  Resource reuse can lead to data leakage between virtual machines.

○  Previously unknown flaws exploited before developers can fix them.

○  Notable examples include the BEAST and POODLE attacks. ○

Ethical disclosure aims to limit potential harm.

○  Common cause of security vulnerabilities.

○  Default configurations often prioritize usability over security. ○

Proper configuration and change management are crucial.

○  Weaknesses in cryptographic systems, algorithms, or protocols.

○  Examples include MD5, SHA-1, and RSA vulnerabilities. ○

Proper key generation and protection are essential.

○  Methods to gain elevated privileges on mobile devices.

○  Introduces security risks, including malware installation and data breaches. ○

Violates terms of service and voids warranties on some platforms.

Susceptible to common vulnerabilities like insecure Wi-Fi and phishing attacks.

More likely to be lost or stolen, exposing data if unencrypted.

6. Zero-Day Vulnerabilities:
4. Firmware Vulnerabilities:
5. Virtualization Vulnerabilities:
8. Cryptographic Vulnerabilities:
10. Mobile Device Vulnerabilities:
7. Misconfiguration Vulnerabilities:
9. Sideloading, Rooting, and Jailbreaking:
## Page 36

●

●

●

○

○  Definition: Update containing harmful code disguised as legitimate.

○  Purpose: Distribution of malware, execution of cyberattacks.

○  Examples: CCleaner compromise (2017), SolarWinds attack (2020).

○  Mitigation: Secure software supply chain management, digital signature

verification.

Evaluation Scope:○  Definition: Analysis of product, system, or service for vulnerabilities.

○  Targets: Software application, network, security service, or IT infrastructure. ○

Goals: Identify weaknesses, ensure compliance with security standards.

○  Security Testing: Vulnerability assessments, penetration testing.

○  Documentation Review: Ensure implementation according to secure design

principles.

○  Source Code Analysis: Identify security vulnerabilities in code.

○  Configuration Assessment: Evaluate security-related configurations.

○  Cryptographic Analysis: Assess encryption mechanisms and key management.

○  Compliance Verification: Ensure compliance with relevant regulations.

○  Security Architecture Review: Evaluate security controls and design.

○  Scope: Defines objectives for penetration tester or attacker.

○  Penetration Tester: Authorized to evaluate system, report findings, recommend

remediation.

TOE Practice Description:

Penetration Tester vs. Attacker:

Application and Cloud Vulnerabilities

●  Malicious Update:

## Page 37

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Attacker: Aims to exploit vulnerabilities within target for unauthorized access or

- ther malicious objectives.
Definition: Target applications accessible over the Internet.

Characteristics: Exploit poor input validation, misconfigured security settings,

- utdated software.
Examples: XSS, CSRF, improper session management.

Types: Reflected/nonpersistent, stored/persistent, DOM-based.

Execution: Injects malicious scripts into trusted sites, executed in client's browser.

Exploits: Unsecure handling of SQL queries.

Impact: Unauthorized access to database, data theft, execution of arbitrary code.

Targets: Cloud-hosted applications.

Exploits: Misconfigurations, weak authentication, insufficient network

segmentation.

Characteristics: Shared responsibility model, scalability attracts attackers.

Definition: Mediate access to cloud services by users.

Functions: Single sign-on authentication, malware scanning, activity monitoring.

Implementation: Forward proxy, reverse proxy, API-based.

Definition: Risks and weaknesses introduced into software products during

development, distribution, maintenance.

Components: Service providers, hardware suppliers, software providers.

Importance: Transparency, visibility, rapid response to vulnerabilities.

Tools: OWASP Dependency-Check, SPDX, OWASP CycloneDX standards for

SBOM creation.

Supply Chain:

SQL Injection (SQLi):

Web Application Attacks:

Cross-Site Scripting (XSS):

Cloud-Based Application Attacks:

Cloud Access Security Brokers (CASBs):

## Page 38

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Designed to test network hosts such as client PCs, servers, routers, and

switches.

Compares scan results to configuration templates and lists of known

vulnerabilities.

Identifies missing patches, deviations from baseline configurations, and related

vulnerabilities.

Examples include Tenable Nessus and OpenVAS.

○  Non-Credentialed Scans:

■  Test packets directed at hosts without login access.

■  View obtained is that of an unprivileged user.

■  Useful for external network perimeter assessment or web application

scanning.

Credentialed Scans:

■  Given user account access with appropriate permissions.

■  Allows in-depth analysis, especially for detecting misconfigurations.

■  Mimics insider attacks or compromised user accounts.

Specialized for identifying software application weaknesses.

Includes static analysis (reviewing code) and dynamic analysis (testing running

applications).

Identifies issues like unvalidated inputs, broken access controls, and SQL

injection vulnerabilities.

Tracks and assesses security of third-party software packages, libraries, and

dependencies.

Ensures they are up to date and free from known vulnerabilities.

Associated with software bill of materials (SBOM) and software supply chain risk

management.

Real-time, continuously updated sources of information about potential threats

and vulnerabilities.

Integrated into vulnerability management practices for swift response to emerging

risks.

Gathered from security vendors, cybersecurity organizations, and open-source

intelligence.

Threat Feeds

Package Monitoring

Credentialed vs. Non-Credentialed Scans

Application and Web Application Scanners

Vulnerability Identification Methods

●  Network Vulnerability Scanner

## Page 39

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

:

Evaluates vulnerabilities for potential impact and exploitability.

Considers factors like ease of exploitation, potential damage, asset value, and

current threat landscape.

○  Collects and analyzes publicly available information for decision-making.

○  Used in cybersecurity to identify vulnerabilities and threat information. ○

Sources include blogs, forums, social media, and the dark web.

Aggressive approach to vulnerability management.

Involves ethical hacking to breach security and exploit vulnerabilities.

Identifies complex vulnerabilities that automated tools may miss.

Incentivizes external security researchers to discover and report vulnerabilities.

Complements penetration testing with a global community of researchers.

Encourages responsible disclosure of verified security issues.

Essential part of vulnerability management.

Includes product audits, system/process audits, and security audits.

Penetration testing is a critical component of technical and compliance audits.

Auditing

Bug Bounties

Penetration Testing

Vulnerability Analysis and Remediation

●  Vulnerability Analysis

Open-Source Intelligence (OSINT)

Vulnerability Analysis and Remediation

## Page 40

●

●

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

:

Updated via SCAP, facilitating sharing of intelligence data.

Consist of common identifiers for vulnerability descriptions.

:

Maintained by NIST, provides detailed vulnerability information.

Supplements CVE descriptions with additional analysis and CVSS metrics.

:

Generates a score from 0 to 10 based on vulnerability characteristics.

Score bands: 0.1+ (Low), 4.0+ (Medium), 7.0+ (High), 9.0+ (Critical).

:

Incorrect identification of vulnerabilities by scanners.

Can lead to unnecessary time and effort if not addressed.

:

Undetected vulnerabilities in scans.

Risk mitigated by periodic rescanning and using scanners from different vendors.

:

Validates vulnerability reports by examining system and network logs.

Confirms vulnerability alerts and ensures accurate remediation.

Helps prioritize remediation efforts by addressing critical vulnerabilities first.

:

Mitigation techniques include patching, configuration changes, software updates,

- r system replacement.
Compensating controls provide alternative plans when immediate remediation is

impossible.

Verification of successful remediation via rescanning affected systems.

:

Identifies critical vulnerabilities for focused remediation efforts.

:

Categorizes vulnerabilities based on characteristics for clarity.

:

Assesses susceptibility of assets to specific vulnerabilities.

:

Evaluates potential organizational impact for informed decision-making.

:

Includes IT infrastructure, external threat landscape, regulatory environment, and

- perational practices.
Log Review

Remediation

False Negatives

Vulnerability Analysis

Prioritization

Classification

Exposure Factor

Impacts

Environmental Variables

National Vulnerability Database (NVD)

Common Vulnerabilities and Exposures (CVE)

●  Vulnerability Feeds

False Positives, False Negatives, and Log Review

●  False Positives

CVSS (Common Vulnerability Scoring System)

## Page 41

●

●

○

○

○

:

Patching, cybersecurity insurance, segmentation, compensating controls,

exceptions, and exemptions.

:

Ensures remediation actions are implemented correctly and do not introduce

new vulnerabilities.

:

Highlights existing vulnerabilities, ranks based on severity, provides

recommendations, and emphasizes timely reporting for effective remediation.

Hardening Concepts:

●  Default settings in network equipment, software, and operating systems balance ease of

use with security.

●  Default configurations are often targeted by attackers due to well-documented

credentials, insecure protocols, etc.

●  Hardening involves changing default settings to enhance security, typically following

published secure baselines.

Switches and Routers Hardening:

●  Change default credentials to mitigate security risks.

Validation

Reporting

Vulnerability Response and Remediation

●  Remediation Practices

Evaluate Network Security Capabilities

Network Security Baselines

## Page 42

●

●

●

●

○

Disable unnecessary services like HTTP or Telnet to reduce attack surface.

Use secure management protocols like SSH instead of Telnet.

Implement Access Control Lists (ACLs) to restrict access.

Enable logging and monitoring to identify security issues.

## Page 43

Configure port security to limit device connections.

●  Implement strong password policies.

●  Physically secure equipment to prevent unauthorized access.

Server Hardware and Operating Systems Hardening:

●  Change default credentials to prevent unauthorized access.

●  Disable unnecessary services to reduce attack surface.

●  Apply software security patches and updates regularly.

●  Implement the least privilege principle.

●  Use firewalls and Intrusion Detection Systems (IDS) to block or alert on malicious

activity.

●  Secure configurations using baseline configurations like CIS or STIGs.

●  Implement strong access controls like strong password policies, MFA, and PAM.

●  Enable logging and monitoring for identifying security issues.

●  Use antivirus and antimalware solutions to detect and quarantine malware. ●  Physically

secure server equipment to prevent unauthorized access.

Wireless Network Installation Considerations:

●  Ensure good coverage of authorized Wi-Fi access points to prevent rogue and evil twin

attacks.

●  Use nonoverlapping channels in the 5 GHz band for better performance.

●  Conduct site surveys to measure signal strength and interference.

●  Use heat maps to optimize WAP placement and configuration.

●  Configure wireless encryption settings to secure the network.

●  Consider vulnerabilities and limitations of Wi-Fi Protected Setup (WPS). ●  Utilize Wi-Fi

Protected Access 3 (WPA3) for improved security.

Wi-Fi Authentication Methods:

● Pe rsonal, open, and enterprise authentication types.

●  WPA2-PSK and WPA3-SAE for personal authentication.

●  WPA3 enhances security over WPA2, particularly with SAE protocol.

●  Enterprise authentication involves 802.1x, EAP methods, and RADIUS.

Network Access Control (NAC):

Authenticates users and devices, enforces compliance with security policies.

Restricts access based on user profile, device type, location, etc.

Works with VLANs to automate security measures.

NAC can be agent-based or agentless, each with its advantages and limitations.

●

●

●

●

## Page 44

●

●

●

●

●

●

●

●

●

ACLs control traffic at a network interface level using packet information like

source/destination IP addresses, port numbers, and protocols.

Firewall rules dictate how firewalls handle inbound/outbound traffic based on IP

addresses, port numbers, protocols, or application traffic patterns.

Rules in a firewall's ACL are processed from top to bottom; specific rules are placed at

the top, and a default deny rule is typically at the end.

Basic principles include blocking internal/private IP addresses, protocols for local

network level, penetration testing, and securing hardware.

Firewalls, IDS, IPS, and web filters are essential components in network security.

Firewalls create a barrier between trusted internal networks and untrusted external

networks, controlling incoming and outgoing traffic based on rules.

IDS monitor network traffic for possible incidents and alert administrators.

IPS not only detect but also prevent threats by taking automated actions like blocking

traffic.

Web filters control access to Internet content, preventing access to malicious websites

and monitoring access to restricted sites.

Network Security Capability Enhancement

Screened Subnet:

Access Control Lists (ACL):

Network Security Capability Enhancement:

## Page 45

●

●

●

●

●

●

●

●

●

●

●

●

●

Snort and Suricata are well-known IDS/IPS tools.

Security Onion provides intrusion detection, network security monitoring, and log

management.

These tools use signature-based, behavioral/anomaly-based, and trend analysis

detection methods.

IDS/IPS monitor network traffic for suspicious patterns or activities.

Host-based (HIDS/HIPS) installed on individual systems detect insider threats, file

changes, and local events.

Network-based (NIDS/NIPS) monitor network traffic for known threats and unusual

behavior across multiple systems.

Acts as a neutral zone between an organization's internal network and the Internet,

separating public-facing servers from sensitive internal resources.

Hosts web, email, DNS, or FTP services accessible from the Internet but isolated from

internal systems to limit damage from breaches.

Firewalls control traffic to/from the screened subnet, providing an additional layer of

protection.

Web filters block access to malicious or inappropriate websites, preventing malware

infections and increasing productivity.

Agent-based filtering installs software agents on devices, enforcing filtering policies

locally.

Centralized web filtering uses proxy servers to analyze and control web traffic,

implementing block rules, content categorization, and reputation-based filtering.

Issues include overblocking, underblocking, handling of encrypted traffic, and privacy

concerns. Proper configuration and management are essential.

IDS/IPS Tools:

Web Filtering:

Intrusion Detection and Prevention Systems (IDS/IPS):

## Page 46

●

●

●

●

●

●

●

●

●

●

●

●

●

Ensures systems adhere to mandatory security configurations.

Allow lists permit execution only for approved applications.

Block lists prohibit execution of listed processes.

Lists need regular updates based on incidents and threat hunting.

may be necessary based on threat analysis.

ACLs manage access control policies for files and directories.

Each object in the file system has an ACL associated with it.

ACLs contain a list of allowed accounts and their permissions.

Permissions include Read (r), Write (w), and Execute (x).

Permissions are applied based on owner user (u), group (g), and others (o).

Commands like chmod modify permissions using symbolic or absolute mode.

Monitoring enforces and maintains security measures on endpoints.

Helps detect changes that weaken security configurations.

compliance and auditing purposes.

●  Provides data for

Strategic changes

Assess Endpoint Security Capabilities

Implement Endpoint Security

Monitoring:

Configuration Enforcement:

ACLs and File System Permissions:

Application Allow Lists and Block Lists:

## Page 47

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Crucial steps in hardening endpoints.

Changing default passwords and removing unnecessary software reduces

vulnerabilities.

Security feature in Linux supporting access control security policies.

Offers granular permission control over processes and system objects.

Limits resource access to prevent harm from malicious or flawed programs.

Involves standardized configuration baselines, automated management tools,

continuous monitoring, and change management processes.

Protects endpoints against evolving cybersecurity threats.

Strategies include physical port hardening, logical port security, encryption, and

hostbased firewalls/IPS.

Involves strategic planning, standardized configurations, automated deployments,

updates, monitoring, and centralized management.

Unique hardening strategies for industrial control systems, embedded systems, real-

time operating systems, and IoT devices.

Involves network segmentation, authentication, secure coding, and compliance with

security standards and certifications.

Centralized management of Windows OS settings in an Active Directory environment.

Applies security settings consistently across systems.

Settings include password policies, firewall settings, software restrictions, etc.

Secure process for retiring devices to prevent data exposure.

Involves data sanitization, resetting to factory settings, and updating inventory records.

SELinux:

Group Policy:

Decommissioning:

Hardening Techniques:

Installing Endpoint Protection:

Hardening Specialized Devices:

Changing Defaults and Removing Unnecessary Software:

## Page 48

2.
Corporate owned, business only (COBO): Device owned by organization, strictly

for business use.

Corporate owned, personally enabled (COPE): Device provided by organization,

allows personal use within policy limits.

Choose your own device (CYOD): Employees select devices from a

predetermined list.

Each model balances control, flexibility, and security differently.

COBO offers more control but higher equipment spending; BYOD offers flexibility

but security challenges.

●

○

○

○

○

○

Mobile Device Hardening

1. Mobile Device Deployment Models:
Mobile Device Management (MDM):

## Page 49

3.
4.
5.
:

Network directory lists subjects (users, computers, services) and objects

(directories, files) with permissions.

Most use Lightweight Directory Access Protocol (LDAP) over port 389.

Authentication methods:

■  No Authentication: Anonymous access.

Crucial for managing, securing, and enforcing policies on smartphones and

tablets.

Maintains device inventory, ensures authorized access, enforces security policies,

and enables remote lock or wipe.

Manages device updates, patches, app distributions, and other tasks.

Various platforms available: Apple’s MDM, Android Enterprise, Microsoft Intune,

VMware AirWatch, IBM MaaS360.

Most mobile OSes offer full device encryption.

iOS offers multiple encryption levels, including Data Protection for sensitive data.

Android encrypts user data at the file level by default (since Android 10).

Care should be taken with external media (MicroSD cards) to apply encryption

where necessary.

Utilizes GPS or Indoor Positioning System (IPS) for device location.

Privacy concerns arise due to tracking potential; apps require user permission.

Geofencing creates virtual boundaries; can be used for context-aware

authentication.

Cellular connections bypass enterprise network protections; require endpoint

controls.

Wi-Fi risks from open access points or rogue networks; strong WPA3 security

recommended.

Bluetooth vulnerabilities include device discovery, authentication issues, malware,

and bluejacking/bluesnarfing.

NFC for short-range communication and mobile payments; vulnerable to

eavesdropping, interception, and data corruption attacks.

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Location Services:

Full Device Encryption and External Media:

Connection Methods (Cellular, Wi-Fi, Bluetooth):

Enhance Application Security Capabilities

Application Protocol Security Baselines

●  Secure Directory Services

## Page 50

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

■  Simple Bind: Plaintext DN and password.

■  SASL: Negotiates supported authentication mechanisms.

■  LDAPS: Uses digital certificate for secure tunnel on port 636.

Limit access: Disable anonymous and simple authentication if secure access is

required.

Access control policy for read-only and read/write access.

Restrict access to private network; block LDAP port from public interface.

:

Framework for management and monitoring.

Agent maintains Management Information Base (MIB); communicates over ports

161 (queries) and 162 (traps).

SNMP Monitor oversees agents, polls them for info, alerts for traps.

Security measures: Disable if not used, use difficult-to-guess community names,

restrict management operations, use SNMP v3 for encryption and strong

authentication.

:

FTP remains popular despite newer protocols.

FTP lacks security mechanisms, vulnerable to interception.

SSH FTP (SFTP) and FTP Over SSL (FTPS) provide encryption.

SFTP uses SSH over port 22; FTPS uses TLS over ports 21 (explicit) and 990

(implicit).

:

SMTP for sending; mailbox protocol (POP3, IMAP) for storing/accessing.

Secure SMTP (SMTPS) and Secure POP (POP3S) use TLS.

Secure IMAP (IMAPS) allows permanent connections and folder management.

Email Security:

■  SPF, DKIM, DMARC authenticate senders, prevent phishing and spam.

■  Email Gateway scrutinizes emails, utilizes anti-spam filters, antivirus

scanners, DMARC, SPF, DKIM.

■  S/MIME encrypts and authenticates email communications.

■  Email Data Loss Prevention (DLP) prevents unauthorized sharing of

sensitive information.

:

Blocks or allows access to specific websites by controlling DNS resolution.

Proactive defense mechanism against phishing sites, malware, and inappropriate

content.

Implemented through DNS filtering services, DNS servers, DNS firewalls, or local

DNS resolvers.

:

Configure DNS servers for fault tolerance, restrict recursive queries to local

hosts.

Patch DNS server software regularly to mitigate vulnerabilities.

Prevent DNS footprinting by applying access control lists to prevent unauthorized

zone transfers.

DNS Security

DNS Filtering

Email Services

File Transfer Services

Simple Network Management Protocol Security (SNMP)

## Page 51

Cloud and web application security involve:

○  Cloud hardening: fortifies cloud infrastructure, reduces attack surface.

○  Application security: ensures secure design, development, deployment.

Both practices establish a layered defense strategy against various threats.

Secure coding practices include:

○  Input validation techniques.

DNSSEC provides validation process for DNS responses, mitigates spoofing and

poisoning attacks.

●

●

●

○

Cloud and Web Application Security Concepts

Concepts:

## Page 52

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

●

Principle of least privilege.

Secure session management.

Encryption enforcement.

Patching support.

Developers should design software with:

Comprehensive, structured, meaningful logs.

Enhance logging, monitoring for better threat detection.

incident response.

Verifies integrity, authenticity of software code.

Uses digital signatures, certificates from trusted CAs.

Assures source, integrity of code, not its safety or security.

Data exposure prevention.

Error handling: Structured exception handling, avoiding default error messages.

Memory management: Avoiding faulty practices.

Client-Side vs. Server-Side Validation: Client-side informs users, server-side validates.

Application Security in the Cloud: Complementary to cloud hardening.

Real-time alerting improves

Real-time alerting mechanisms.

Security considerations for new programming technologies should be understood and

tested.

Modern development practices include security development lifecycle.

Examples: Microsoft’s SDL, OWASP Software Assurance Maturity Model, OWASP Top

10.
Input validation:

○  Essential for addressing untrusted input issues.

○  Techniques: Allowlisting, Blocklisting, Data Type Checks, Range Checks, Regular

Expressions, Encoding.

Secure Cookies:

Principles include 'Secure', 'HttpOnly', 'SameSite' attributes.

Protect against session hijacking, cross-site scripting.

Static Code Analysis:

Identifies vulnerabilities, errors, noncompliant coding practices.

Tools: SonarQube, Coverity, Fortify.

Code Signing:

Software Sandboxing:

Monitoring Capabilities:

Application Protections:

Secure Coding Techniques:

## Page 53

●

●

Isolates processes, prevents access to system.

Implemented in web browsers, operating systems, virtual machines.

●  Essential for malware detection, forensic inspection. ●  Tools: Cuckoo Sandbox, Joe

Sandbox.

These study notes cover the essential concepts and techniques for understanding cloud and

web application security, including secure coding practices, input validation, secure cookies,

static code analysis, code signing, application protections, monitoring capabilities, and software

sandboxing.

Sandboxing in Security Operations:

Incident Response and Monitoring Concepts

Explain Incident Response and Monitoring Concepts

Incident Response

## Page 54

●

●

●

●

●

●

●

●

●

●

●

●

●

● ●

●

Factors affecting impact determination:

○  Data integrity.

○  Downtime.

○  Economic/publicity.

○  Scope.

○  Detection time. ○

Recovery time.

SOPs for specific cyber threat scenarios.

Investigating detected indicators.

Determining genuine incident and priority level.

Categorizing true positive incidents.

Escalating analysis for complex or high-impact events.

Shared understanding of incident terms and concepts.

Relies on threat intelligence for effective analysis.

Utilizes frameworks like cyber kill chain for threat research.

Correlating events from network and system data sources.

Identifying indicators:

○  Matching events in log files, IDS alerts, etc.

○  Deviations from baseline metrics.

○  Proactive threat hunting.

○  Employee, customer, or supplier notifications.

Importance of confidential reporting.

First responder notification crucial for appropriate response.

SIEM platform.

Guide for detection and response steps.

Formal plan listing procedures, contacts, and resources for various incident categories.

Preparation outcome.

Managing alerts through

Impact:

Analysis:

Category:

Detection:

Playbooks:

Containment:

●

Incident Response Plan:

## Page 55

:

Mitigation and restoration steps post-containment.

Reconstitution of affected systems.

Reaudit security controls.

Notification and remediation for affected parties.

Isolation-based and segmentation-based techniques.

Focus on preserving forensic evidence.

Root cause analysis.

Structured inquiry into incident causes.

Staff meeting and report compilation.

Focus on improving procedures rather than blaming individuals.

Proactive discovery of TTPs.

Utilizes threat intelligence and analytics platforms.

Considerations for intelligence fusion and adversary maneuvering.

Validate incident response readiness.

Testing forms: tabletop exercises, walkthroughs, simulations.

Training on incident detection, reporting, and cross-departmental coordination.

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Threat Hunting:

Lessons Learned:

Testing and Training:

Eradication and Recovery:

Introduction to Digital Forensics

Digital Forensics

1.
## Page 56

●

○  Digital forensic analysis involves examining evidence gathered from computer

systems and networks.

## Page 57

2.
3.
4.
5.
6.
7.
8.
9.
10.
Purpose: Uncover relevant information such as deleted files, timestamps, user

activity, and unauthorized traffic.

:

Importance of digital forensic analysis in incident response.

Processes and tools for acquiring digital evidence.

Documentation is critical for collecting, preserving, and presenting valid digital

proofs.

:

Digital forensics for prosecuting crimes, especially insider threats like fraud or

misuse of equipment.

Importance of due process and procedural safeguards to ensure fairness.

Legal hold: Preservation of information relevant to a court case, including

electronic records.

:

Process of obtaining a forensically clean copy of data from seized devices.

Impact of legality on acquisition, especially regarding BYOD policies.

Order of volatility for evidence collection: CPU cache, system memory, mass

storage, remote logging, physical configuration.

:

Importance of volatile data from RAM.

Tools and methods for capturing system memory, such as memory dumps.

:

Acquiring data from nonvolatile storage like hard drives, SSDs, and optical

media.

Live acquisition vs. static acquisition methods.

Imaging tools for bit-level copies of storage media.

:

Ensuring the integrity of evidence by avoiding alterations during acquisition.

Use of write blockers to prevent changes to source data or metadata.

○

:

Cryptographic hashing to ensure data integrity.

Chain of custody documentation to establish proper handling and integrity of

evidence.

:

Ethical principles in analysis: unbiased, repeatable methods, minimal

manipulation of evidence.

Importance of strong documentation and reporting to withstand legal scrutiny.

:

Filtering relevant evidence from forensic examinations.

Functions of e-discovery tools: de-duplication, search, tagging, security,

disclosure.

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

E-Discovery

Disk Image Acquisition

System Memory Acquisition

Due Process and Legal Hold

Incident Response Activities

Reporting in Digital Forensics

Acquisition of Digital Evidence

Preservation of Digital Evidence

Evidence Integrity and Non-Repudiation

## Page 58

1.
Data Sources

Introduction to Metadata:

## Page 59

2.
3.
4.
5.
6.
Metadata is data about data, including properties like creation time, author, and

permissions.

It is crucial for establishing timelines and providing evidence in incident

investigations.

:

Attributes stored by the file system include creation, access, and modification

times.

Security attributes like read-only or hidden, and permissions represented by ACLs.

Extended attributes can include author information, copyright details, or tags for

indexing.

Social Media Metadata:

Metadata uploaded to social media can reveal unintended information like

location and time.

:

Web servers return resource properties via headers in response to client

requests.

Headers can include authorization information, data type (text or binary), and may

be logged by servers.

:

Email headers contain sender, recipient, and transmission details handled by

mail agents.

Mail user agents (MUAs) create initial headers, mail delivery agents (MDAs) add

- r amend headers, and message transfer agents (MTAs) route messages.
Headers can contain additional information added by each MTA along the delivery

path.

:

Headers are not typically exposed to users but can be viewed via message

properties or source command.

MTAs add detailed information to headers, making it difficult to read in plaintext.

Tools like Message Analyzer can parse and display headers in a structured format,

showing the delivery path and added headers.

○

○

○

○

○

○

○

○

○

○

○

○

○

○

File Metadata

Web Metadata

Email Metadata

Viewing and Analyzing Metadata

Agent-Based and Agentless Collection:

Alerting and Monitoring Tools

## Page 60

1.
2.
3.
2.
2.
3.
4.
:

Interprets data from various systems for consistency and searchability.

SIEM features connectors or plug-ins for different systems.

Requires parsers for each data source to map attributes to standard fields.

:

Ensures consistency across different time zones to establish a single timeline.

:

○  Involves installing an agent service on each host.

○  Events on the host are logged, filtered, aggregated, and sent to the SIEM server

for analysis.

○  Typically used for Windows/Linux/macOS computers.

:

○  Hosts push log changes to the SIEM server without installing an agent.

○  Used for devices like switches, routers, and firewalls. ○

Uses Syslog protocol for forwarding logs to SIEM.

:

Collects packet captures and traffic flow data.

Utilizes sniffer tools via mirror port functionality or network tap.

:

○  SIEM runs correlation rules on extracted indicators to detect potential incidents.

○  Correlation involves interpreting relationships between data points.

○  Correlation rules use logical expressions and operators to define conditions.

○  Threat intelligence feeds associate collected data with known threat indicators.

:

○  Includes analysis, containment, eradication, and recovery steps.

○  Validation during analysis confirms true positives. ○

Quarantine isolates the source of indicators.

:

○  Provides insight into security system status.

○  Formats tailored for different audiences like executives, managers, and

compliance regulators.

○  Metrics include authentication data, patch status, incident statistics, and trend

reporting.

:

○  Retains historical log and network traffic data.

Supports retrospective incident and threat hunting and compliance

requirements.

performance.

○  Requires a retention policy to manage data volume and SIEM

○

○

○

○

○

○

Sensor

Archiving

Reporting

Log Aggregation:

1. Normalization
Listener/Collector

Incident Response

Agent-based Collection

Date/Time Normalization

Alerting and Monitoring Activities:

1. Alerting
## Page 61

2.
2.
3.
4.
:

System monitors assess host health status using SNMP traps.

Logs are critical for security information, audit trails, and intrusion detection.

:

Monitor application/service status, bandwidth consumption, and cloud services.

Vulnerability scanners assess host vulnerabilities and misconfigurations.

Antivirus software detects malware and integrates with SIEM for alerting.

:

Controls data copying to restrict it to authorized media and services. ○

Monitoring statistics for DLP policy violations help identify trends.

:

Compare system configurations to established benchmarks for compliance.

Compliance scans ensure conformity to regulatory standards and best practices.

:

Reduces false positives to avoid alert fatigue.

Techniques include refining detection rules, redirecting alerts, and continuous

monitoring.

False negatives are also addressed to prevent overlooking threats.

:

Uses managerial reports for day-to-day monitoring of computer resources and

network infrastructure.

Network monitors collect data about network infrastructure appliances for status

monitoring.

NetFlow provides flow data analysis for network traffic metadata.

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Monitoring Infrastructure

Data Loss Prevention (DLP)

Monitoring Systems and Applications:

1. System Monitors and Logs
Application and Cloud Monitors

Benchmarks and Compliance Scans

Alert Tuning and Monitoring Infrastructure:

1. Alert Tuning
## Page 62

Ransomware encrypts files, demanding payment for decryption; crypto-ransomware

encrypts data and demands ransom in cryptocurrency.

Cryptojacking hijacks resources for cryptocurrency mining, often across botnets.

Logic bombs execute after a set time or event, triggering malicious actions.

Backdoors provide unauthorized access, while Remote Access Trojans (RATs) operate

covertly for administrative control.

Compromised hosts may have bots, forming botnets used for DDoS attacks, spam, or

cryptomining.

RATs connect to a command and control (C&C) host for remote control, often using

covert channels like IRC or HTTPS/DNS.

Trojans requiring user execution inherit user privileges; gaining admin privileges needs

UAC confirmation.

Rootkits operate at the system level, concealing themselves as legitimate processes,

files, or services.

Some rootkits exploit vulnerabilities to gain SYSTEM privileges or reside in firmware for

persistence.

Viruses and worms evolved from destructive replication to facilitating intrusion, fraud,

and data theft.

Tracking cookies record web activity, IP addresses, search queries, etc., while

supercookies and beacons track covertly.

Adware alters browser settings, inserts ads, and changes search providers.

Spyware monitors application activity, captures screenshots, and activates recording

devices like microphones.

Keyloggers record keystrokes to steal confidential information like passwords and credit

card data.

Metasploit Meterpreter tool can be used to dump keystrokes from victim machines.

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Analyze Indicators of Malicious Activity

Malware Attack Indicators

Rootkits:

TTPs and IoCs:

Spyware and Keyloggers:

Backdoors and Remote Access Trojans:

Ransomware, Crypto-Malware, and Logic Bombs:

## Page 63

●

●

●

●

●

Tactics, Techniques, and Procedures (TTPs) describe threat behaviors, methods, and

detailed procedures used by threat actors.

Indicators of Compromise (IoCs) are residual signs of successful or ongoing attacks,

including compromised processes, connections to C&C networks, and altered system

settings.

Sandboxes isolate and analyze suspicious code; resource consumption, file system

changes, and account compromise indicate malicious activity.

Access denial, resource inaccessibility, and suspicious account behavior like lockouts or

impossible travel suggest a security breach.

Threat actors may attempt to cover their tracks by deleting or altering logs, leading to

missing or manipulated log entries.

Malicious Activity Indicators:

## Page 64

●

●

●

●

●

●

■

■

○  Targets subnet's default gateway.

○  If successful, attacker intercepts traffic destined for remote networks. ○ Implemented through ARP poisoning to perform on-path attack.

○  Exploit weaknesses in Domain Name System (DNS).

○  Various types: typosquatting, DRDoS, DoS against public DNS services, DNS

server hijacking.

○  DNS poisoning compromises name resolution process.

○  Methods: on-path attacks, DNS client cache poisoning, DNS server cache

poisoning.

○  Rogue Access Points:

■  Unauthorized access points installed on the network.

■  Can be malicious or accidental.

■  Evil twin mimics legitimate access point to deceive users.

○  Wireless Denial of Service:

■  Disrupts wireless networks using interference or spoofed frames.

○  Wireless Replay and Key Recovery:

■  Exploits lack of encryption in management frame traffic.

■  Disassociation attacks disconnect clients.

■  Aimed at recovering network keys.

○  Online Attacks:

■  Interact directly with authentication service.

■  Mitigated by limiting login attempts.

○  Offline Attacks:

■  Exploit obtained password hashes.

■  Utilize packet sniffers or access to password databases.

○  Brute Force, Dictionary, Hybrid Attacks:

■  Attempt every combination or use dictionary words. ○

Password Spraying:

■  Tries common passwords with multiple usernames.

○  Target Windows Active Directory networks.

○  Exploit cached credentials to gain access to other hosts. ○

Types: pass the hash, golden ticket, silver ticket attacks.

○  Downgrade Attacks:

Forces use of weaker protocols or ciphers.

○  Collision Attacks:

Exploits weak hashing functions to create same hash for different inputs.

Physical and Network Attack Indicators

DNS Attacks:

Wireless Attacks:

Password Attacks:

ARP Poisoning Attack:

Cryptographic Attacks:

Credential Replay Attacks:

## Page 65

●

○

○

○

○

Birthday Attacks:

■  Exploits collisions in hash functions through brute force.

Types of malicious activity: shellcode, credential dumping, pivoting/lateral

movement, persistence.

Indicators found in endpoint protection software or network logs.

Malware interacts with network, file system, and registry.

Malicious Code Indicators:

## Page 66

2.
3.
4.
5.
6.
7.
8.
:

Application attacks target vulnerabilities in OS or application software.

Vulnerabilities can lead to compromised security systems or application crashes.

Main scenarios: compromising OS or third-party apps, compromising website or

web application security.

:

Increased application crashes/errors can indicate exploitation attempts.

Anomalous CPU, memory, storage, or network utilization can also be indicators.

Indicators may be found in system logs or application-specific logs.

:

Goal: Allow threat actors to run their own code on the system.

Types: Vertical (elevation) and horizontal privilege escalation.

Indicators: Process logging, audit logs, incident response, and endpoint protection

agents.

:

Exploits vulnerabilities by overwriting data in a buffer.

Common vulnerability: stack overflow.

Mitigation: Address Space Layout Randomization (ASLR) and Data Execution

Prevention (DEP).

:

Exploit session mechanisms like cookies.

Session token identification and exploitation.

:

CSRF: Exploits cookies for unauthorized actions.

SSRF: Causes server to process arbitrary requests targeting other services.

:

Exploits unsecure application request processing.

Types include XML Injection, LDAP Injection, Directory Traversal, and Command

Injection.

:

HTTP request structure and methods.

Percent encoding and its misuse for obfuscation.

Web server logs as indicators of attacks, including status codes and HTTP header

information.

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Application Attack Indicators

Summarize Security Governance Concepts

Policies, Standards, and Procedures

Security Governance Concepts

URL Analysis

Replay Attacks

Forgery Attacks

Buffer Overflow

Injection Attacks

Privilege Escalation

1. Importance of Standards
1. Application Attacks Overview
Indicators of Application Attacks

## Page 67

2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
○  Stakeholders influence standards choice.

○  Standards reflect dedication to quality, security, reliability.

○  Strategic selection based on legal, business, risk management, and stakeholder

needs.

○  Adoption impacts operations; appropriate selection enhances effectiveness.

○  ISO/IEC 27001, 27002, 27017, 27018.

○  NIST Special Publication 800-63.

○  PCI DSS.

○  FIPS.

○  Audit compliance and security practices; assess adherence and identify gaps.

○  Password standards: hashing, salting, transmission, reset, managers.

○  Access control standards: models, verification, privilege management,

authentication, session management, audit trails.

○  Building, workstation, datacenter security. ○  Equipment disposal, visitor

management.

○  Algorithms, key length, management.

○  Governance committees ensure compliance with laws and regulations.

○  Legislation examples: Sarbanes-Oxley Act, Computer Security Act, Federal

Information Security Management Act.

○  International laws like GDPR and CCPA protect privacy globally.

○  Laws like GDPR and CCPA have international reach.

○  GDPR emphasizes informed consent, data subject rights.

○  CCPA empowers California residents with data control rights.

○  National, local, regional laws vary; compliance essential.

○  Examples: HIPAA, GLBA, FISMA, Data Protection Act, PIPEDA, IT Act.

○  Examples across healthcare, finance, telecommunications, energy, education,

government sectors.

○  Compliance ensures industry-specific data protection.

○  Ensures compliance with laws and regulations.

○  Continuous monitoring, evaluation, and updating essential. ○

Governance boards, committees crucial for oversight.

Centralized: unified decision-making; standardized practices.

Decentralized: localized decision-making; adaptability.

Hybrid models combine elements for flexibility and standardization.

○

○

○

Global Law

Internal Standards

Industry Standards

Encryption Standards

Legal Environment

Regulations and Laws

Physical Security Standards

Industry-Specific Regulations

Governance and Accountability

Centralized vs. Decentralized Governance

## Page 68

12.
13.
Ensure efficient and effective handling of changes.

Minimize risks associated with changes.

Regulatory, intelligence, law enforcement, defense agencies involved.

Data protection authorities enforce regulations.

National cybersecurity agencies focus on critical infrastructure protection.

Owner: strategic guidance.

Controller: legal and regulatory compliance.

Processor: secure data handling.

Custodian: implementation and enforcement of security controls.

Systematic approach to managing changes in IT infrastructure.

Goal: Minimize risk and disruption, maximize value and efficiency of changes.

Relies on planning, testing, approval, and implementation.

Considers impacts, dependencies, and develops contingency plans. ●  Requires proper

documentation and communication.

●

●

●

●

●

●

○

○

○

○

○

○

○

Data Governance Roles

2. Change Management Programs:
Government Entities and Groups

Study Notes on Change Management:

1. Importance of Change Management:
Change Management

## Page 69

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Begins with submitting a Request for Change (RFC).

Reviewed by designated change manager or committee.

Formal approval involving stakeholders.

Documentation and communication throughout the process.

Involvement of stakeholders from various parts of the organization.

Ensures comprehensive review of proposed changes.

Promotes acceptance and adoption of changes. ●  Facilitates ownership and

responsibility.

Allow lists: Approved changes exempt from full change management process.

Manage various changes including software deployments, updates, hardware

replacements, etc.

Prevent introduction of vulnerabilities, service disruptions, or compliance issues.

Impact Analysis: Identifying and assessing potential implications of proposed changes.

Test Results: Evaluation of changes in a test environment before implementation.

Backout Plans: Contingency plans for reversing changes if implementation fails.

Maintenance Windows: Predefined time frames for implementing changes.

Standard Operating Procedures (SOPs): Detailed instructions for implementing changes

consistently.

6. Allowed and Blocked Changes:
5. Change Management Concepts:
4. Factors Driving Change Management:
3. Change Management Approval Process:
## Page 70

●

●

●

●

●

●

●

●

●

●

Unique challenges in managing changes due to outdated technology and lack of

support.

Requires specialized solutions and extensive testing.

Deny lists: Explicitly blocked changes requiring full change management process.

Ensure control over authorized and unauthorized changes.

Considerations for minimizing disruptions during change implementation.

Scheduled maintenance windows and minimizing impacts on business operations.

Understanding dependencies to mitigate unintended outages.

Tracking and controlling changes to documents, code, or data.

Ensures historical record of changes, consistency, and quick reversion to previous

versions.

Impacts various documentation including change requests, policies, system

documentation, etc.

8. Legacy Systems and Applications:
9. Documentation and Version Control:
7. Restarts, Dependencies, and Downtime:
Study Notes on Automation and Orchestration:

Automation and Orchestration

## Page 71

Tools for managing security operations efficiently.

Automation: Performs repetitive, rule-based tasks to reduce human error.

Orchestration: Coordinates interactions between automated processes and systems.

Enhances efficiency, reduces errors, and provides clear audit trails.

Complexity: Requires deep understanding of systems and processes.

Cost: Initial investment in tools, integration, and training can be high.

Single Point of Failure: Critical automated systems failing could cause widespread

problems.

Technical Debt: Hasty implementation leading to poorly documented code or system

instability.

Ongoing Support: Requires continuous updates, patches, and maintenance for

effectiveness.

Provisioning: Automating user and resource provisioning tasks to reduce manual effort

and errors.

Guardrails and Security Groups: Automating monitoring and enforcement of security

policies.

Ticketing: Automating incident detection, ticket generation, routing, and escalation

procedures.

Service Management: Automating routine tasks to free up time for strategic analysis.

Continuous Integration and Testing: Automation improves code quality and accelerates

development cycles.

Application Programming Interfaces (APIs): Automation orchestrates interactions

between software systems.

Enhances efficiency by reducing repetitive tasks and human error.

Combats operator fatigue in security operations.

Improves security posture by enforcing standardized baselines and automating security

tasks.

Supports staff retention initiatives by reducing fatigue from repetitive tasks.

Critical tools in modern IT operations for streamlining processes and enhancing security.

Enhances security governance by enforcing policies consistently.

Aids in change management by reducing implementation time and providing audit trails.

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

2. Automation and Scripting:
3. Capabilities of Automation:
4. Benefits of Automation and Orchestration:
5. Challenges of Automation and Orchestration:
1. Importance of Automation and Orchestration:
## Page 72

●

●

●

●

●

Ensures consistency and accuracy throughout the infrastructure.

Saves time and resources by quickly deploying configurations.

Enhances scalability, flexibility, standardization, compliance, and change management.

Strengthens security and governance by enforcing security controls and applying

patches consistently.

1. Risk Management Overview:
6. Benefits of Infrastructure Management Automation:
Explain Risk Management Processes

Risk Management Processes and Concepts

## Page 73

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

●

Residual Risk: Likelihood and impact after mitigation measures.

Risk Appetite: Strategic assessment of tolerable residual risk levels.

BIA: Identifying and assessing impact of disruptions on business operations.

MEFs: Functions critical for business continuity that cannot be deferred.

Identification of Mission Essential Functions (MEFs) and vulnerabilities.

Analysis of threats, business impacts, and risk responses.

Assessing likelihood and impact of risks using qualitative and quantitative methods.

Risk management frameworks like NIST RMF or ISO 31K guide processes.

Risk Registers: Documents results of risk assessments, including severity, mitigation

strategies, and ownership.

Proactive and systematic approaches to identify, assess, prioritize, and mitigate risks.

Risk mitigation involves reducing exposure to or the effects of risk factors.

Maximum Tolerable Downtime (MTD), Recovery Time Objective (RTO), Work Recovery

Time (WRT), Recovery Point Objective (RPO).

Mean Time to Repair (MTTR) and Mean Time Between Failures (MTBF) as KPIs for

system reliability and efficiency.

Risk Threshold: Defines acceptable risk levels based on various factors.

KRIs: Predictive indicators to monitor and predict potential risks, supporting proactive

risk management.

Risk Deterrence/Reduction: Controls to make risk incidents less likely or less costly.

Avoidance: Stopping activities causing risk, although infrequently a credible option.

Risk Transference: Assigning risk to a third party, such as through insurance.

Risk Acceptance/Tolerance: No countermeasures put in place due to risk level

●

justification.

Risk Exceptions/Exemptions: Formal recognition of risks that cannot be mitigated within

specified conditions.

2. Risk Management Strategies:
4. Risk Management Processes:
3. Residual Risk and Risk Appetite:
7. Key Metrics in Risk Management:
5. Risk Threshold and Key Risk Indicators (KRIs):
6. Business Impact Analysis (BIA) and Mission Essential Functions (MEFs):
## Page 74

●

●

○

■

■

■

Third-party risk assessment involves:

Vendor due diligence.

Risk identification and assessment.

Ongoing monitoring.

Vendor Management Concepts

Vendor Management Concepts:

## Page 75

●

○

○

○

○

○

○

○

○

■  Incident response planning.

Vendor due diligence includes evaluating:

■  Security practices.

■  Financial stability.

■  Regulatory compliance.

■  Reputation.

Risk identification and assessment involve:

■  Identifying potential risks.

■  Assessing impact on operations, data, and reputation.

Ongoing monitoring ensures:

■  Vendors maintain security controls.

■  Adhere to contractual obligations.

■  Promptly address identified risks or vulnerabilities.

Critical in risk management to:

■  Identify, assess, and mitigate risks.

■  Implement robust assessment processes.

■  Maintain regulatory compliance.

■  Foster a safe operational environment.

Systematically evaluate potential vendors.

Steps include: ■  Identifying risk criteria.

■  Conducting due diligence.

■  Selecting vendors based on risk profile.

Aims to identify and mitigate risks related to:

■  Financial stability.

■  Operational reliability.

■  Data security.

■  Regulatory compliance.

■  Reputation.

Select vendors aligning with:

Vendor Selection:

## Page 76

●

○

○

○

○

○

○

■  Organization’s risk tolerance.

■  Effective risk management capability.

External entities providing goods, services, or technology.

Offer specialized expertise and support.

Range from technology providers to suppliers.

Bring efficiency, cost-effectiveness, and innovation.

Introduce potential risks:

■  Access to sensitive data.

■  Infrastructure.

■  Critical processes.

Proper assessment ensures adherence to security standards, compliance, and

fulfillment of obligations.

Third-Party Vendor Assessment:

## Page 77

2.
3.
4.
5.
2.
3.
○  Ensure operations align with standards, policies, and regulations.

○  Identify gaps and provide recommendations for improvement.

○  Enhance security measures by assessing effectiveness and efficiency.

○  Attestation verifies security controls' accuracy and compliance.

○  Independent examination assures stakeholders of security measures.

○  Internal assessments by employees ensure continuous improvement.

○  External assessments by third-party providers offer impartial evaluation. ○

Both methods complement each other for comprehensive evaluation.

Compliance Assessment: Ensures alignment with laws, regulations, and policies.

Audit Committee: Provides oversight and assurance on financial practices.

Self-Assessment: Allows for internal evaluation of performance and practices.

Regulatory Assessments: Ensure compliance with laws and industry standards.

Examination: Independent evaluation of financial statements and controls.

Assessment: Broad evaluation of performance, practices, and capabilities.

Third-Party Audit: Objective assessment by external entities for compliance.

Simulate real-world attacks to identify vulnerabilities and weaknesses.

Test specific systems, incident response capabilities, and physical controls.

Offensive Penetration Testing (Red Teaming): Mimics potential attackers' tactics.

Defensive Penetration Testing (Blue Teaming): Evaluates defensive measures.

Physical Penetration Testing: Assesses physical security practices and controls.

Integrated Penetration Testing: Holistic approach combining different

methodologies.

○

○

○

○

○

○

○

○

○

○

○

○

○

Audits and Assessments

Types of Penetration Testing:

Attestation and Assessments:

Study Notes on Penetration Testing:

1. Purpose of Penetration Testing:
Internal Assessment Approaches:

External Assessment Approaches:

Internal vs. External Assessments:

1. Purpose of Audits and Assessments:
Active and Passive Reconnaissance:

## Page 78

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

4.
Active: Probing and interacting with target systems to gather information.

Passive: Gathering information without directly interacting, focusing on publicly

available data.

Known Environment: Detailed knowledge about the target system or network.

Partially Known Environment: Limited knowledge requiring reconnaissance.

Unknown Environment: Little prior knowledge to simulate real-world scenarios.

Occurs when information is read, modified, or deleted without authorization.

Includes loss of any type of data, especially corporate and intellectual property.

Privacy breach specifically refers to loss or disclosure of personal and sensitive

data.

Reputation damage: Leads to negative publicity and loss of customer trust.

Identity theft: Can result in lawsuits for damages.

Fines: Regulators may impose fixed sums or a percentage of turnover.

IP theft: Loss of revenue due to theft of copyrighted material or corporate data.

Requirements set by law or regulations dictate who must be notified.

Breach can include loss, theft, or accidental disclosure of information.

Accidental breaches pose substantial risks if effective procedures are lacking.

Breach may be considered even with potential for unauthorized access.

Even minor breaches should be escalated to senior decision-makers.

Impact from legislation and regulation should be considered.

Notification to law enforcement, affected individuals, third-party companies, and

the public may be required.

Legislation sets out requirements and timescales for notifications.

Disclosure includes description of breached information, contact details,

consequences, and mitigation measures.

Escalation:

Compliance:

Notifications of Breaches:

Definition of Data Breach:

Public Notification and Disclosure:

Organizational Consequences of Breaches:

Known, Partially Known, and Unknown Testing Methods:

Summarize Data Protection and Compliance

Concepts

Data Classification and Compliance

## Page 79

○  Refers to adherence to security standards, regulations, and best practices.

## Page 80

●

●

●

●

●

●

●

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

○

Requires establishment of policies, procedures, controls, and technical

measures.

Noncompliance can result in legal sanctions, financial penalties, reputational

damage, and loss of customer trust.

Geographic restrictions, encryption, hashing, masking, tokenization, obfuscation,

segmentation, permission restrictions.

Automates discovery, classification, and enforcement of data protection rules.

Components include policy server, endpoint agents, and network agents.

Remediation actions include alerting, blocking, quarantining, and tombstoning.

Portable devices like smartphones, USB sticks, etc., pose security threats due to

easy file copying and potential camera/voice recording functions.

Solutions like network access control, endpoint management, and data loss

prevention can help prevent attachment of such devices to corporate networks.

Companies may struggle to enforce policies against bringing personal devices

- nsite.
Unauthorized use of personal software (shadow IT) can lead to security

vulnerabilities and legal liabilities for the organization.

Requires employees to keep their work areas free from documents to prevent

unauthorized access to sensitive information.

Essential for ensuring users understand security policies, incident reporting, site

security procedures, data handling, password/account management, social

engineering threats, etc.

Training should be tailored to different job roles' security requirements and levels

- f expertise.
Use a variety of techniques like workshops, one-on-one instruction,

computerbased training, videos, etc., to improve engagement and retention.

Computer-based training can include simulations and branching scenarios to

practice cybersecurity tasks.

Includes policy training, situational awareness, insider threat education,

password management, and training on handling removable media and cables.

Also covers social engineering tactics, operational security, and training for

hybrid/remote work environments.

Clean Desk Policy:

Data Protection Methods:

Data Loss Prevention (DLP):

User and Role-Based Training:

Training Topics and Techniques:

Personally Owned Devices in the Workplace:

Critical Elements for Security Awareness Training:

Personnel Policies

## Page 81

●

●

●

●

●

○

○

○

○

○

○

Simulated phishing attacks are used to raise awareness about phishing risks

among employees.

Training helps employees recognize and respond effectively to phishing

attempts, reducing the likelihood of data breaches.

Training focuses on identifying unusual actions or patterns that could indicate

security threats.

Employees learn to recognize and report risky, unexpected, and unintentional

behaviors that could lead to security incidents.

Follows stages of assessing security needs, planning, development, delivery,

evaluation, reinforcement, and monitoring/adaptation to ensure effectiveness.

Emphasizes creating engaging materials, incorporating real-world examples, and

facilitating discussions to enhance learning.

Methods include assessments, incident reporting analysis, phishing simulations,

- bservations/feedback, and tracking metrics like training completion rates.
○

Phishing Campaigns:

Reporting and Monitoring:

Security Awareness Training Lifecycle:

Development and Execution of Training:

Anomalous Behavior and Recognizing Risky Behaviors:
