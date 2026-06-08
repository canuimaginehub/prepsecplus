# CompTIA Security Plus+ Master Cheat Sheet

## Page 1

1 | P a g e

### Skillcertpro

COMPTIA Security Plus+ Master

Cheat Sheet

1.0 Threats, Attacks and Vulnerabilities
1. Given a scenario, analyze indicators of compromise and determine the type of malware.
1. Viruses: An unsolicited and unwanted malicious program.
2. Crypto-malware: A malicious program that encrypts programs and files on the computer in order to
extort money from the user.

3. Ransomware: Denies access to a computer system or data until a ransom is paid. Can be spread
through a phishing email or unknowingly infected website.

4. Worm: A self-contained infection that can spread itself through networks, emails, and messages.
5. Trojan: A form of malware that pretends to be a harmless application.
6. Rootkit: A backdoor program that allows full remote access to a system.
7. Keylogger: A malicious program that saves all of the keystrokes of the infected machine.
8. Adware: A program that produces ads and pop ups using your browser, may replace the original
browser and produce fake ads to remove the adware in order to download more malware.

9. Spyware: Software that installs itself to spy on the infected machine, sends the stolen information
- ver the internet back to the host machine.
10. Bots: AI that when inside an infected machine performs specific actions as a part of a larger entity
known as a botnet.

11. RAT (Remote Access Trojan): A remotely operated Trojan.
12. Logic bomb: A malicious program that lies dormant until a specific date or event occurs.
13. Backdoor: Allows for full access to a system remotely.
2. Compare and contrast types of attacks.
1. Social engineering: Gathering information on an attack by exploiting the weakest part of security,
people.

1. Phishing: Sending a false email pretending to be legitimate to steal valuable information
from the user.

2. Spear phishing: Attacks that target specific users.
3. Whaling: An attack on a powerful or wealthy individual.
4. Vishing: An attack through a phone or voice communications.
5. Tailgating: Closely following individuals with keys to get access to secure areas.
6. Impersonation: Taking on the identity of an individual to get access into the system or
communications protocol.

7. Dumpster diving: Going through a business’s or person’s trash to find thrown away valuable
information or possessions.

8. Shoulder surfing: Watching as a person enters information.
9. Hoax: False information that deceives the user into compromising security by making them
believe they are at risk.

10. Watering hole attack: A security attack that targets a specific highly secured group by
infecting a commonly visited website by the group’s members.

11. Principles (reasons for effectiveness):
1. Authority: The actor acts as an individual of authority.
2. Intimidation: Frightening or threatening the victim.
3. Consensus: Influenced by what others do, everyone else does it.
## Page 2

2 | P a g e

### Skillcertpro

4. Scarcity: Limited resources and time to act.
5. Familiarity: The victim is well known.
6. Trust: Gain their confidence, be their friend.
7. Urgency: Limited time to act, rush the victim.
2. Application/service attacks:
1. DoS (Denial of Service): Flooding a target machine or resource with many requests to
- verload the system and prevent use of its resources.
2. DDoS (Distributed Denial of Service): Multiple different sources attack one victim.
3. Man-in-the-middle: The attacker alters the communication between two parties who believe
they are directly communicating.

4. Buffer overflow: A program attempts to write more data than can be held in fixed block of
memory.

5. Injection: Occurs from processing invalid data, inserts code into the vulnerable computer
program and changes the course of execution.

6. Cross-site scripting (XXS): Found in web applications, allows for an attacker to inject client -
side scripts in web pages.

7. Cross-site request forgery (XSRF): Unauthorized commands are sent from a user that is
trusted by the website. Allows the attacker to steal cookies and harvest passwords.

8. Privilege escalation: An attack that exploits a vulnerability that allows them to gain access to
resources that they normally would be restricted from accessing.

9. ARP poisoning: The act of falsifying the IP-to-MAC address resolution system employed by
TCP/IP.

10. Amplification: The amount of traffic sent by the attacker is originally small but then is
repeatability multiplied to place a massive strain on the victim’s resources, in an attempt to

cause it to fail or malfunction.

11. DNS poisoning: Is a type of attack that exploits vulnerabilities in the domain name system
(DNS) to divert Internet traffic away from legitimate servers and towards fake ones.

12. Domain hijacking: The act of changing the registration of a domain name without the
permission of the victim.

13. Man-in-the-browser: A proxy Trojan horse that infects web browsers and capture browser
session data

14. Zero day: The aim is to exploit flaws or vulnerabilities in targeted systems that are unknown
- r undisclosed to the world in general. Meaning that there is no direct or specific defense to
the attack; which puts most systems vulnerable assets at risk.

15. Replay: Is a network-based attack where a valid data transmission is rebroadcasted,
repeated, or delayed.

16. Pass the hash: An authentication attack that captures and uses the hash of a password. The
attacker then attempts to log on as the user with the stolen hash. This type of attack is

commonly associated with the Microsoft NTLM (New Technology LAN Manager) protoco l.

17. Hijacking and related attacks:
1. Clickjacking: Deceives the user into clicking on a malicious link by adding the link
to a transparent layer over what appears to be a legitimate web page.

2. Session hijacking: An attack in which an attacker attempts to impersonate the
user by using their legitimate session token.

3. URL hijacking: Redirects the user to a false website based on misspelling the
URL, and is also referred to typosquatting.

4. Typosquatting: An alternate name for URL hijacking.
18. Driver manipulation:
1. Shimming: The process of injecting alternate or compensation code into a system
in order to alter its operations without changing the original or existing code.

## Page 3

3 | P a g e

### Skillcertpro

2. Refactoring: Rewrites the internal processing of code without changing its
behavior.

19. MAC spoofing: The attacker falsifies the MAC address of a device.
20. IP spoofing: An intruder uses another site's IP address to masquerade  as a legitimate site.
3. Wireless attacks:
1. Replay: This is a passive attack where the attacker captures wireless data, records it, and
then sends it on to the original recipient without them being aware of the attacker's

presence.

2. IV (Initialization Vector): A random number used to increase security by reducing
predictability and repeatability.

3. Evil twin: Has same SSID (Service Set Identifier) as a proper access point (AP). Once a user
connects to it, all wireless traffic goes through it instead of the real AP.

4. Rogue AP (Access Point): An unauthorized WAP (Wireless Access Point) or Wireless Router
that allows for attackers to bypass many of the network security configurations and opens

the network and its users to attacks.

5. Jamming: Disabling a wireless frequency with noise to block the wireless traffic.
6. WPS (WiFi Protected Setup): Allows users to easily configure a wireless network, sometimes
by using only a PIN. The PIN can be found through a brute force attack.

7. Bluejacking: Sending unauthorized messages to a Bluetooth device.
8. Bluesnarfing: Gaining unauthorized access to, or stealing information from a Bluetooth
device

9. RFID (Radio Frequency Identifier): Communicates with a tag placed in or attached to an
- bject using radio signals. Can be jammed with noise interference, the blocking of radio
signals, or removing/disabling the tags themselves.

10. NFC (Near Field Communication): A wireless technology that allows for smartphones and
- ther devices to establish communication over a short distance.
11. Disassociation: Removes clients from a wireless network.
4. Cryptographic attacks
1. Birthday: Used to find collisions in hashes and allows the attacker to be abl e to create the
same hash as the user. Exploits that if the same mathematical function is performed on two

values and the result is the same, then the original values are the same.

2. Known plain text/cipher text:
1. Plain text: The attacker has both the plaintext and its encrypted version.
2. Cipher text: The attacker has access only to the encrypted messages.
3. Rainbow tables: Large pregenerated data sets of encrypted passwords used in password
attacks.

4. Dictionary: A password attack that creates encrypted versions of common dictionary words
and then compares them against those in a stolen password file. Guessing using a list of

possible passwords.

5. Brute force: A password-cracking program that tries every possible combination of
characters through A to Z.

6. Online vs. offline:
1. Online: Is against a live logon prompt.
2. Offline: The attack is working on their own independent computers to
compromise a password hash.

7. Collision: When two different inputs produce the same hash value.
## Page 4

4 | P a g e

### Skillcertpro

8. Downgrade: Forces a system to lessen its security, this allows for the attacker to exploit the
lesser security control. It is most often associated with cryptographic attacks due to weak

implementations of cipher suites. Example is TLS > SSL, a man -in-the-middle POODLE attack

exploiting TLS v1.0 - CBC mode.

9. Replay: The attacker captures network packets and then retransmits them back onto the
network to gain unauthorized access.

10. Weak implementations: The main cause of failures in modern cryptography systems are
because of poor or weak implementations instead of a failure caused by the algorithm itself.

3. Explain threat actor types and attributes.
1. Script kiddies: A person who uses pre-existing code and scripts to hack into machines, because they
lack the expertise to write their own.

2. Hacktivist: An individual who is someone who misuses computer systems for a socially or
politically motivated agenda. They have roots in the hacker culture and ethics. Hacker on a mission.

3. Organized crime: These are professionals motivated ultimately by profit. They have  enough money to
buy the best gear and tech. Multiple people perform specific roles: gathering data, managing exploits,

and one who actually writes the code.

4. Nation states/APT: An APT is an advanced persistent threat, these are massive security risks that can
cost companies and countries millions of dollars. Nation states have very sophisticated hacking teams

that target the security of other nations. They often attack military organizations or large security

sites, they also frequently attack power plants.

5. Insiders: Someone who is inside the company who has intricate knowledge of the company and how
its network works. They can pinpoint a specific vulnerability and may even have access to multiple

parts of the network.

6. Competitors: Rival companies, can bring down your network or steal information through espionage.
7. Internal/external: Internal is inside the company, can be intentional, unintentional, or an act of God.
External is someone outside the company trying to get in.

8. Level of sophistication: Is the skill of the hacker and the complexity of the attack.
9. Resources/funding: The amount of money and the value of the tech and gear being used.
10. Intent/motivation: The reason for the attack, can be for political, monetary, or social reasons.
11. Use of open-source intelligence (OSINT): Data that is collected through publicly available information.
This can be used to help make decisions. Can be used by threat actors to help find their next target or

how to best attack their target. OSINT is also incredibly helpful for mitigating risks and for identifying

new threat actors.

4. Explain penetration testing concepts.
1. Active reconnaissance: Is the use of tools to send data to systems and then understanding their
responses. Usually starts with various network and vulnerability scanners. Can be incredibly illegal

and should not be engaged without being prepared and proper authorization.

2. Passive reconnaissance: You are not touching any of the target’s equipment. Instead you are going
through and gathering that is already available. Forums and social media are great sources for

gathering information about the company and its employees.

3. Pivot: In penetration testing it is using a compromised machine to attack other machines on the same
network. Attacking and gaining access to an area of lower security in order to be more likely to have a

successful attack on an area of greater security. Is also referred to as island hopping.

4. Initial exploitation: Usually the hardest part. A vulnerability is taken advantage of to get into the
network or system.

5. Persistence: Installing backdoors or methods to keep access to the host or networks.
6. Escalation of privilege: Allows for a user to get a higher-level access than what authentication allows
for. Can be resolved through patching and updating. Typ ically related to a bug or vulnerability

7. Black box: You know nothing of the network, you have no prior knowledge.
8. White box: You are given a network map and you have full knowledge of the configurations allowing
you to perform specific tests.

9. Gray box: Knowledge of the network but not incredibly detailed.
## Page 5

5 | P a g e

### Skillcertpro

10. Penetration testing vs. vulnerability scanning: Penetration testing is an active attack on the network
to exploit vulnerabilities, can assess potential damages and the potential of the exploits being found.

Is done by a human. Vulnerability scans passively scans and identifies vulnerabilities. Is automated.

5. Explain vulnerability scanning concepts.
1. Passively test security controls: Uses an automated vulnerability scanner. Observes and reports
findings. Does not take down systems, applications, or services, and doesn’t disrupt business.

2. Identify vulnerability: Understanding common attacks and taking inventory of vulnerabilities.
Scanners can report: missing updates, misconfigured security settings, and kn own exploits.

3. Identify lack of security controls: Vulnerability scanners can identify missing patches or antivirus.
4. Identify common misconfigurations: Weak passwords, default usernames and passwords, and open
ports.

5. Intrusive vs. non-intrusive: Intrusive testing can interrupt service, is much more detailed, and exploits
vulnerabilities. Non-intrusive is more passive, does not exploit vulnerabilities, and does not disrupt

service.

6. Credentialed vs. non-credentialed: Credentialed are done as though it is inside the network, emulates
an insider attack. Non-credentialed are done as though it is outside the network, emulates an outside

attack. Shows what would be found if the network was scanned.

7. False positive: A result which shows incorrectly that a condition or  attribute is present. A false
vulnerability.

6. Explain the impact associated with types of vulnerabilities
1. Race conditions: The behavior of a software, electronic, or another system’s output is dependent on
the timing, sequence of events, or a factor out of the user’s control.

2. Vulnerabilities due to:
1. End-of-life systems: No longer receives updates, and at a high risk to compromise.
2. Embedded systems: Programs added for automation and/or monitoring. Can allow for
malicious programs to gain access through the added programs.

3. Lack of vendor support: Vendor does not support the product: does not update, improve, or
protect the product.

3. Improper input handling: The system does not properly validate data, allows for an attacker to create
an input that is not expected. Allows for parts of the system vulnerable to unintended data.

4. Improper error handling: The error messages display sensitive or private information that give the
user too much data.

5. Misconfiguration/weak configuration:
6. Default configuration: Uses the unsecure out-of-box settings.
7. Resource exhaustion: A denial of service occurs, the amount of resources to execute an action are
expended, making it unable for the action to be performed.

8. Untrained users: Users are not properly informed on how to use the systems. This means that
mistakes will more likely occur and that the system’s resources may be abused.

9. Improperly configured accounts: Users should only be allowed to access the parts that they need to
complete their work.

10. Vulnerable business processes: All tasks, procedures, and functions should be properly assessed and
the most valuable and vulnerable should be heavily protected.

11. Weak cipher suites and implementations: Use of older and less robust cryptographic algorithms. EX.
### Des, Wep

12. Memory/buffer vulnerability:
1. Memory leak: Leaves the system unresponsive.
2. Integer overflow: Large integer exceeds data storage capacity.
3. Buffer overflow: Too much data for the computer’s memory to buffer.
## Page 6

6 | P a g e

### Skillcertpro

4. Pointer dereference: Failed deference can cause memory corruption and t he application to
crash.

5. DLL injection: Allows for the running of outside code.
13. System sprawl/undocumented assets: Lack of internal inventory and allowing unsecure devices and
systems to connect to the network.

14. Architecture/design weaknesses: An insecure and poorly designed network. Ex. Not segmenting the
systems or internal network.

15. New threats/zero day: A zero-day threat, is a flaw that is unknown to the teams patching and fixing
flaws.

16. Improper certificate and key management: Allowing for unauthorized access to certificates and keys,
which allows for sensitive data to be decrypted. And allowing for certificates to expire.

2.0 Technologies and Tools Install and configure network components,
1. Hardware and software-based, to support organizational security.
1. Firewall: A network security system that monitors and controls incoming and outgoing network traffic
based on predetermined security rules.

1. ACL (Access control lists): A list of rules that can be used to control traffic based on networks,
subnets, IP addresses, ports, and some protocols.

2. Application-based vs. network-based:
1. Application-based: Protects the user from applications and services by monitoring
and potentially blocking the input, output, or system service calls that do not

meet the configured policy of the firewall.

2. Network-based: Filtering traffic based on firewall rules and allows only authorized
traffic to pass in and out of the network

3. Stateful vs. stateless:
1. Stateful: Stateful firewalls block traffic based on the state of the packet within a
session. It adds and maintains information about a user's connections in a state

table, referred to as a connection table.

2. Stateless: Stateless firewalls uses rules within an ACL to identify allowed and/or
block traffic through packet filtering.

4. Implicit deny: The last rule in an ACL that indicates that, "all traffic that isn't explicitly allowed
is implicitly denied".

2. VPN concentrator: A type of router device that allows for the secure creation of VPN connections and
for the safe delivery of messages between VPN nodes. Allows for the handling of a large quantity of

VPN tunnels.

1. Remote access vs. site-to-site:
1. Remote access: A user-to-LAN connection used by remote users.
2. Site-to-site: Allows multiple sites to connect to remote sites over the internet.
2. IPSec: A protocol suite for securing Internet Protocol (IP) communications. Encrypts and
authenticates all of the packets in a session between hosts or networks. Secures more

applications than SSL and TLS.

3. Tunnel mode: The default mode for IPSec, the entire pack is protected.
## Page 7

7 | P a g e

### Skillcertpro

4. Transport mode: Used for end-to-end communications in IPSec. Ex. encrypted Telnet or
Remote Desktop session from a workstation to a server.

5. Authentication Header (AH): IPsec protocol that authenticates that the packets received
were sent from the source identified in the header.

6. ESP (Encapsulating Security Payload): IPSec component that provides the same services as
AH and also ensures confidentiality when sending data.

7. Split tunnel vs. full tunnel:
1. Split tunnel: Only some traffic over the secure VPN while the rest of the traffic
directly accesses the internet.

2. Full tunnel: All of the traffic is sent over the secure VPN.
8. TLS: The replacement of SSL to encrypt data-in-transit. Uses certificates issued by CAs.
9. Always-on VPN: The user does not connect and disconnect and instead is always connected.
3. NIPS (Network Intrusion Prevention System)/NIDS (Network Intrusion Detection System):
1. Signature-based: Detects attacks based on known attack patterns documented as attack
signatures.

2. Heuristic/behavioral: It detects attacks by comparing traffic against a baseline to find any
anomalies.

3. Anomaly: Abnormal packets or traffic.
4. Inline vs. passive:
1. Inline: Connected directly to the network and monitors the flow of data as it
- ccurs.
2. Passive: Connected through a switch or port on the network and receives a copy
- f the flow of data as it occurs.
5. In-band vs. out-of-band:
1. In-band: Sits in the network, can quickly warn of or prevent malicious traffic.
2. Out-of-band: Out the can only warn of malicious traffic.
6. Rules: Standards set to differentiate good traffic from suspicious traffic.
7. Analytics: Shows the amount, type and history of traffic coming through.
8. False positive: NIPS blocks legitimate incoming traffic.
9. False negative: NIPS allows harmful incoming traffic.
4. Router: A device that directs data traffic along specific routes.
1. ACLs (Access Control List): A list of permit or deny rules detailing what can or can't enter or
leave the interface.

2. Anti-Spoofing: A device with the intent of excluding packets that have inva lid source
addresses.

5. Switch: A networking device that connects devices together on a computer network
1. Port security: Requires a username and a password and authenticate before gaining access
to any of the switch interfaces.

2. Layer 2 vs. Layer 3:
1. Layer 2: Packets are sent to a specific switch port based on destination MAC
addresses.

## Page 8

8 | P a g e

### Skillcertpro

2. Layer 3: Packets are sent to a specific next-hop IP address, based on destination IP
address.

3. Loop prevention: Spanning-tree algorithms can determine the best path to a host while
blocking all other paths to prevent loops. Loops can cause a denial of service.

4. Flood guard: Configuration that sets the maximum number of MAC addresses that could
possibly be seen on any particular interface.

6. Proxy: Acts as an intermediary for requests from clients seeking resources from servers that provide
those resources.

1. Forward and reverse proxy:
1. Forward proxy:  Forwards requests from internal clients to external servers.
2. Reverse proxy: Takes in requests from the Internet and forwards them to an
internal web server.

2. Transparent: Accepts and forwards requests without performing any modifications on them.
3. Application/multipurpose: A type of proxy server that knows the application protocols that it
supports.

7. Load balancer: A reverse proxy that distributes network or application traffic across a number of
servers designed to increase capacity of concurrent users and reliability of applications.

1. Scheduling: Sends requests to servers using set rules.
2. Affinity: Sends client requests to the same server based on the client's IP address.
3. Round-robin: Sends requests in a predefined order.
4. Active-passive: Some servers are not active and only go active to take excess traffic or if an
active server fails.

5. Active-active: All servers are actively processing requests
6. Virtual IPs: An IP address and a specific port number that can be used to reference different
physical servers. Provides IP addresses that can float between two or more physical network

nodes and provide redundancy.

8. Access point:
1. SSID: Name of a wireless network.
2. MAC filtering: A method of controlling access on a wired or wireless network by denying
unapproved MAC address access to a device.

3. Signal strength: The quality and distance of a signal.
4. Band selection/width: Can be set between 2.4 GHz and 5 GHz depending on which 802.11
protocol is being used.

5. Antenna types and placement:
6. Fat vs. thin:
1. Fat: Has everything necessary to handle wireless clients. If end-user deploys
several Fat Wireless Access Points, each one needs to be configured individual ly.

2. Thin: Acts as a radio and antenna that is controlled by a wireless switch. If
multiple thin wireless access points are deployed, the entire configuration takes

place at the switch. This is the far cheaper option.

7. Controller-based vs. standalone:
1. Controller-based: Require a controller for centralized management and are not
manually configured.

## Page 9

9 | P a g e

### Skillcertpro

2. Standalone: Do not require a controller and are generally used in smaller
environments.

9. SIEM (Security Information and Event Management):
1. Aggregation: The gathering of log and event data from the different network security devices
used on the network.

2. Correlation: Relating various events to identifiable patterns. If those patterns threaten
security, then action must be taken.

3. Automated alerting and triggers: Sends messages based on configured rules based on events
that occur within the log files.

4. Time synchronization: Ensures that the time is the same across devices so that all security
events are recorded at the same time using Network Time Protocol.

5. Event deduplication: Trimming event logging so that the same event is not recorded over and
- ver again, overflowing log space.
6. Logs/WORM: Prevents alteration of logs and archives the source logs with write protection.
10. DLP (Data Loss Prevention): Policies and technologies that protect data loss through theft or
destruction.

1. USB blocking: Prevents the use of USBs
2. Cloud-based: Prevents sensitive data from being stored on the cloud without proper
encryptions and authorization.

3. Email: Protects against email fraud and from valuable data from being sent through email.
11. NAC (Network Access Control): Enforces security policies on devices that access networks to increase
network visibility and reduce risk.

1. Dissolvable vs. permanent:
1. Dissolvable: Disappears after reporting information to the NAC device.
2. Permanent: Resides on end devices until uninstalled.
2. Host health checks: Reports sent by network access control to gather information on
installed devices.

3. Agent vs. agentless:
1. Agent: Is installed on the end device.
2. Agentless: Is not installed on the device itself but instead is embedded within a
Microsoft Windows Active Directory domain controller.

12. Mail gateway: Examines and processes all incoming and outgoing email.
1. Spam filter: An on-premises software solution for filtering, well spam emails.
2. DLP (Data Loss Prevention): Prevents certain information leaving the organization via email.
3. Encryption: Encrypt and decrypts emails being sent and received across networks.
13. Bridge: Provides interconnection with other bridge networks using the same protocol.
14. SSL/TLS accelerators: The process of offloading processor-intensive public-key encryption for TLS or
its SSL to a hardware accelerator.

15. SSL decryptors: Allows for the user to view inside of passing Secure HTTP traffic.
16. Media gateway: Converts media streams between disparate telecommunications technologies.
17. Hardware security module: Safeguards and manages digital keys for strong authentication and
provides cryptoprocessing.

## Page 10

10 | P a g e

### Skillcertpro

2. Given a scenario, use appropriate software tools to assess the security posture of an organization.
1. Protocol analyzer: Hardware or software that captures packets to decode and analyze their contents.
Allows for you to easily view traffic patterns, identify unknown traffic, and verify packet filtering and

security controls.

1. Big data analytics: Allows for the user to store large amounts of data and then easily go
through it.

2. Network scanners: A computer program used for scanning
networks to obtain user names, host names, groups, shares, and services.

1. Rogue system detection: Find devices that are not supposed to be on the network, such
as rogue AP’s.

2. Network mapping: Identifying all devices on a network along with a list of ports on those
devices.

3. Wireless scanners/cracker:
1. Wireless scanners: Is for wireless monitoring, it scans wireless frequency bands in order to
help discover rogue APs and crack passwords used by wireless APs.

2. Wireless cracker: Uses wireless attacks to test if an attacker could find the passwords to gain
access to parts of your network.

1. • WEP - Cryptographic vulnerabilities, is relatively straightforward.
2. • WPA1 PSK and WPA2 PSK, uses dictionary brute force and rainbow tables
attacks.

4. Password cracker: A program that uses the file of hashed passwords, such as a rainbow table, and
then attempts to break the hashed passwords of the network. Getting the hashes is the hardest part.

5. Vulnerability scanner: Attempts to identify vulnerabilities, misconfigured systems, and the lack of
security controls such as up-to-date patches. They can be passive or active, either way they have little

impact on a system during the test.

6. Configuration compliance scanner: A vulnerability scanner that verifies systems are configured
correctly and meet the minimum-security configurations, it typically does this by comparing the

system to a file that has the proper configurations. This is an ongoing task and can be integrated with

the logon process.

7. Exploitation frameworks: An already created set of exploits that already have all the major
components designed, the user just needs to figure out how to inject them into the network. These

toolsets can be used offensively by hackers or defensively by pen testers.

8. Data sanitization tools: Tools that overwrite data on hard drives so that it is unrecoverable, this only
needs to be done once but some may do it multiple times to feel safe.

9. Steganography tools: Allows for the user to embed data into an image, video, sound files, or packets.
It is security through obscurity.

10. Honeypot: Decoy systems or networks to gather information on  the attacker.
11. Backup utilities: Important to protect data from being lost, downtime, or corrupted.
12. Banner grabbing: The process of capturing the initial message (the banner) from a network service.
Often the banner discloses the application's identity, version information, and other sensitive

information.

13. Passive vs. active:
1. Passive: You are observing.
2. Active: You are interacting with the network by sending traffic and trying to access parts of
the network.

## Page 11

11 | P a g e

### Skillcertpro

14. Command line tools:
1. ping: The name is based on the sound made by sonar. Tests reachability, it is a primary
troubleshooting tool.

2. netstat (Network statistics):
1. netstat -a:  Show all active connections.
2. netstat -b:  Show binaries, for Windows.
3. netstat -n: Does not resolve names.
3. tracert (Windows)/traceroute (MacOS/Linux): Uses the ICMP (Internet Control Message
Protocol) time to live (TTL) error message to map the path of a packet. Time in TTL is

measured in hops, TTL = 1 for the first router, and 2 refers to the second router.

4. nslookup/dig (Domain Information Groper):
1. nslookup: Used to gather information from DNS servers, lookups names and IP
addresses. Was replaced by dig.

2. dig (Domain Information Groper): More advanced than nslookup and shows more
detailed domain information. Is for Linux but can be downloaded for windows.

5. arp (Address Resolution Protocol): Used to view MAC addresses.
1. Arp -a: Views the local arp table.
6. ipconfig/ip/ifconfig:
1. ipconfig: Shows the Windows TCP/IP configuration.
2. ip: Used to replace ifconfig on Linux. Shows and manipulates settings on the
network interface card (NIC).

3. ifconfig: Shows the Linux interface configuration.
7. tcpdump: A command-line packet analyzer that allows to capture packets from the
command line.

8. nmap: It is designed to scan a network and create a map, this is useful as a vulnerability
scanner because it can find open ports and unsecured access points.

9. netcat: Is used to safely connect to remote systems using command line instead of a front -
end application. Can also be used for banner grabbing.

3. Given a scenario, troubleshoot common security issues.
1. Unencrypted credentials/clear text:  All authentication must be encrypted. Unencrypted credentials
can allow for the attacker to: elevate privileges, establish a foothold, maintain persistence, and move

to other networks.

2. Logs and events anomalies: Block all outside access until the issue is fixed, backup and preserve the
current logs, and if possible, restrict access to more sensitive data till the issue is fixed.

3. Permission issues: Determine how much access a specific user needs to be able to complete their job.
Confirm permissions on initial configurations, perform periodic audits, and provide a process for

changes and updates.

4. Access violations: Segmentation fault, OS locks you out, or prevents access to restricted memory. A
user is able to properly logon and then access systems they don’t have proper authorization for.

5. Certificate issues: Certificates should be signed by someone trusted, be up to date, and be properly
checked.

6. Data exfiltration: Data is your most important asset to and attackers.
7. Misconfigured devices:
## Page 12

12 | P a g e

### Skillcertpro

1. Firewall: Provide too much access, and to audit when using a large rule base,
2. Content filter: URLs are not specific, and some protocols are not filtered.
3. Access points: No encryption mechanisms and Open configurations from the wireless side.
8. Weak security configurations: Make sure to regularly upgrade equipment and update firmware. Using
hash algorithms that are susceptible to collisions.

9. Personnel issues: The weakest link
1. Policy violation: Transferring private data or visiting unsafe websites.
2. Insider threat: Authenticated users have free reign. Assign correct user rights and
permissions.

3. Social engineering: Deceit can cause employees to give up personal or valuable data.
4. Social media: Sharing private data or personal information.
5. Personal email: Uses company resources and leaves the network vulnerable.
10. Unauthorized software: Don’t know what it is: could conflict with company software, could be
malware, or could be useful for work.

11. Baseline deviation: Everything is well documented, any changes to the norm should be noted, and no
remote access until it matches the baseline.

12. License compliance violation (availability/integrity): Make sure licenses are up to date and valid.
13. Asset management: Identify and track assets to respond faster to security risks. Keep detailed records
- f the most valuable assets. Usually automated.
14. Authentication issues: The more factors the safer, makes sure the user is actually the correct person.
4. Given a scenario, analyze and interpret output from security technologies.
1. HIDS/HIPS:
1. HIDS (Host-based intrusion detection system): Runs on a single computer and alerts of
potential threats to help warn of attacks against that host.

2. HIPS (Host-based intrusion prevention system: Runs on a single computer and intercepts
potential threats to help prevent attacks against that host.

2. Antivirus: Software that is specifically designed to detect viruses and protect a computer and files
from harm.

3. File integrity check: An application that can verify that the files have not been modified using hash
algorithms to authenticate the file.

4. Host-based firewall:  A firewall that is on a single host that only restricts incoming and outgoing
network activity for that host.

5. Application whitelisting: The practice of allowing only approved programs to run on a computer,
computer network, or mobile device.

6. Removable media control: Blocks users from using USB drives, CD/DVD drives or portable hard
drives/flash drives to help prevent the installation of viruses, malware, and exfiltration of data.

7. Advanced malware tools: Block malware from running by blocking file signature,
heuristics/Anomalous behavior, sandboxing, virtualizing. Need to be routinely updated with the latest

definitions to be secure and protect against current threats.

8. Patch management tools: Tools that aid in the: monitoring, evaluating, testing, and installing of the
most current software patches and updates.

9. UTM (Unified Threat Management): A group of security controls combined in a  single solution that
can inspect data streams for malicious content and block it.

10. DLP (Data Loss Prevention): Systems that identify, monitor, and protect data: from unauthorized use,
transfers, modification, or destruction.

11. Data execution prevention (DEP): Memory regions are marked as non-executable which prevents
code from being executed. This protects against memory abuse attacks such as buffer overflows.

## Page 13

13 | P a g e

### Skillcertpro

12. Web application firewall: A firewall that looks monitors and filters packets carrying HTTP traffic u sing
a set of communication rules.

5. Given a scenario, deploy mobile devices securely.
1. Connection methods
1. Cellular: Network used for mobile phones.
1. Potential Risks: Cellular devices are susceptible to traffic monitoring, location
tracking, and gain access to the device from anywhere in the world.

2. WiFi: A local area network that uses high frequency radio signals to transmit and receive data
- ver distances of a few hundred feet.
1. Potential Risks: If the Wi-Fi connection is not encrypted it is vulnerable to
eavesdropping. Jamming frequencies or interferences can cause a denial of

service.

3. SATCOM: Satellite Communications that is used for communications in remote areas and
during natural disasters.

1. Potential Risks: SATCOM devices are at risk of leaking geopositioning data and
remote code execution, and are not easily updated remotely.

4. Bluetooth: Allows electronic devices like cell phones and computers to exchange data over
short distances using radio waves.

5. NFC (Near Field Communication): Enable two electronic devices in short proximity to
each other. Typically used as a payment system, but can also be used as an identity token

and to help pair Bluetooth devices.

1. Potential Risks: Active devices can perform a remote capture up to a ten meter
range. Jamming frequencies or interferences can cause a denial of service. Can be

vulnerable to relay and replay attacks.

6. ANT: A wireless sensor protocol that uses a 2.4 GHz ISM (industrial, scientific, and medical)
band to communicate. Used in heart monitors, sports and fitness sensors.

1. Potential Risks: At risk of jamming band, and eavesdropping because encryption is
vulnerable.

7. Infrared: Electromagnetic waves of frequencies lower than the red of visible light. Used to
control entertainment devices and other IR devices.

8. USB (Universal Serial Bus): A cable used to connect mobile devices to other devices. Is
comparatively safer than wireless because it requires a physical connection and data is not

allowed to be transferred without being unlocked first.

1. Potential Risks: Mobile devices can appear as storage devices allowing for the
exfiltration and theft of data.

2. Mobile device management concepts:
1. Application management: Limiting which applications can be installed on a device.
## Page 14

14 | P a g e

### Skillcertpro

2. Content management: Limiting access to content hosted on company systems, and
controlling access to company data stored on mobile devices.

3. Remote wipe: Allows for the deletion of all data and possibly even configuration settings
from a device remotely.

4. Geofencing: Using GPS to define geographical boundaries where the app can be used.
5. Geolocation: The location of a device identified by GPS.
6. Screen locks: Prevents someone from being able to pick up and use a mobile device.
7. Push notification services: Using SMS texts to send messages to selected users or  groups.
8. Passwords and pins: Keep the device safe with something you know.
9. Biometrics: Keep the device safe with something you are.
10. Context-aware authentication: Uses multiple elements to authenticate a user and a mobile
device.

11. Containerization: isolating and protecting the application, including any data used by the
application.

12. Storage segmentation: Separates the information on a device into partitions.
13. Full device encryption: Protects against loss of confidentiality
3. Enforcement and monitoring for:
1. Third-party app stores:  Anything that isn’t from the Apple's App Store or Google Play. More
likely to be a risk to security.

2. Rooting/jailbreaking:
1. Rooting: Android, the process of modifying the device to gain root-level (full
administrator) access.

2. Jailbreaking: Apple, the process removing all software restrictions from the
device.

3. Sideloading: The process of copying an application package to a mobile device.
4. Custom firmware: The removal of the pre-installed firmware and replacing it. This may
remove bloatware included by the vendor or telco, add or remove features, and streamline

the OS to optimize performance.

5. Carrier unlocking: Means the device can be used by any carrier. Most cellular devices only
work with specific carriers.

6. Firmware OTA updates: The downloading of: upgrades, patches, and improvements to the
existing firmware.

7. Camera use: A cable used to connect mobile devices to other devices.
8. SMS/MMS: Sending alerts through text messages.
9. External media: Disable it to prevent the transferring of files through physical ports.
10. USB OTG (Universal Serial Bus On-The-Go):
11. A cable used to connect mobile devices to other devices. It is one of many methods that you
can use to connect a mobile device to external media.

12. Recording microphone: Disable it to prevent people from being able to listen in on
conversations.

13. GPS tagging: Adding GPS information to the video, photo giving its location
14. WiFi direct/ad hoc: Means for wireless devices to connect directly to each other without a
wireless access point.

15. Tethering: The process of sharing an Internet connection from one mobile device to another.
16. Payment methods:
4. Deployment models:
1. BYOD (Bring Your Own Device): Employees to connect their own personal devices to the
corporate network to work.

2. COPE (Corporate Owned, Personally Enabled): Are owned by the organization, but can be
used personally by employees.

## Page 15

15 | P a g e

### Skillcertpro

3. CYOD (Choose Your Own Device): Employees can purchase devices on the list and bring them
to work.  The company then supports, monitors, and manages the device.

4. Corporate-owned: Company owns and controls all aspects, no personal info at all, most
secure for company.

5. VDI (Virtual Desktop Infrastructure): A virtual desktop that is created so users can access
their desktop from a mobile device.

6. Given a scenario, implement secure protocols.
1. Protocols:
1. DNS (Domain Name Service): Does not have any security in its original design. The
hierarchical and decentralized naming system for computers, services, or other resources

connected to a private network or the internet.

2. DNSSEC (Domain Name Service Security Extensions): Primary purpose is to provide a reliable
authorization service between devices when performing operations on the DNS. Must be

digitally signed.

3. SSH (Secure Shell): Replaces Telnet. TCP (Transmission Control Protoc ol) over Port 22.  Allows
for a securely encrypted terminal connection.

4. S/MIME (Secure/Multipurpose Internet Mail Extensions): Digitally signed email content using
public key encryption.

5. SRTP (Secure Real-time Transport Protocol): Protected and encrypted voice communications.
6. LDAPS (Lightweight Directory Access Protocol Secure): TCP ports 389 and 636. Protocol used
for reading and writing directories over an IP network. Uses the X.500 specifications written

by the International Telecommunications Union (ITU) over SSL/TLS.

7. FTPS (File Transfer Protocol Secure): TCP Ports 989/990. File transfer using SSL/TLS.
8. SFTP (Secure File Transfer Protocol): TCP Port 22. FTP over an SSH channel.
9. SNMPv3 (Simple Network Management Protocol Version 3): Ports 161/162. Encrypte d
statistics gathering from a router.

10. SSL (Secure Sockets Layer)/TLS (Transport Layer Security):
1. SSL (Secure Sockets Layer): Encryption technology developed for web and email
- ver the transport layer. Uses public keys to exchange symmetric keys.
2. TLS (Transport Layer Security): The replacement for SSL, is sometimes called SSL
still. Used to encrypt the communication of servers in an organization.

11. HTTPS (Hypertext Transfer Protocol Secure): TCP port 443. HTTP over SSL/TLS provides a
secure connection between the server and web browser.

12. Secure POP (Post Office Protocol)/IMAP (Internet Message Access Protocol):
1. Secure POP (Post Office Protocol): Sends from port 110 to 995. Encrypted email
communications used for retrieving email from a mail server over SSL/TLS.

2. Secure IMAP (Internet Message Access Protocol): Sends from port 143 to 993. Is
standard email protocol for storing email messages on a mail server over SSL/TLS.

2. Use cases:
1. Voice and video: SRTP.
2. Time synchronization: NTPsec.
1. NTPsec (Secure network time protocol): Used to securely sync all the devices’
clocks on the network.

3. Email and web: S/MIME and HTTPS.
4. File transfer:  FTPS or SFTP.
## Page 16

16 | P a g e

### Skillcertpro

5. Directory services: LDAPS or SASL.
1. SASL (Simple Authentication and Security Layer): Provides a source of additio nal
authentication using many different methods, such as Kerberos or client

certificates.

6. Remote access: SSH.
7. Domain name resolution: DNSSec.
8. Routing and switching: SNMPv3, SSH, or HTTPS.
1. SNMPv3: Provides continentality, integrity, and authentication.
2. HTTPS: Allows for browser-based management.
9. Network address allocation: DHCP, there is no secure version it.
1. DHCP starvation attack: Using spoofed MAC addresses to exhaust the amount of
DHCP’s pool. Can configure a switch to limit the number of MAC addresses on an

interface.

10. Subscription services: Anti-viruses and anti-malware are subscription based. Must check
regularly for updates. Set up integrity checks to verify the updates are coming from the

correct source.

3.0 Architecture and Design
1. Explain use cases and purpose for frameworks, best practices and secure configuration guides.
1. Industry-standard frameworks and reference architectures:
1. Framework: Is a collection of standardized policies, procedures and guides, meant to direct a:
user, firm, or any organization.

2. Regulatory: Is a framework that is based on mandated laws and regulations.  HIPAA is an
example of this.

3. Non-regulatory:  The common standards and best practices that the organization follows.
4. National vs. international:
1. National: Framework based on the laws of a single country.
2. International: Framework based on the laws of multiple countries.
5. Industry-specific frameworks: Frameworks based on the standards and regulations of a
certain industry.

2. Benchmarks/secure configuration guides: Instructions that have been developed over years that are
designed to give organizations the best and most secure configurations for a particular system.

1. Platform/vendor-specific guides: Hardening guides that are specific to the software or
platform, also you can get feedback from the manufacturer or internet interest groups.

System default configurations are unsecured and at high risk for exploits.

2. Web server: Web application firewall (WAF), DMZ, Reverse Proxy for incoming
communication from the internet to the server.

3. Operating system: Implement a change management policy.
4. Application server: Securing an application server means using industry standard guides,
vendor specific, locking down the server to only the ports it needs for its specific role.

## Page 17

17 | P a g e

### Skillcertpro

5. Network infrastructure devices: Use national vs international guides, regulatory/non -
regulatory and general purpose guides for securing.

6. General purpose guides: Security configuration guides that are generic in scope.
3. Defense-in-depth/layered security:
1. Vendor diversity: The practice of implementing security controls from different vendors to
increase security. Reduces the impact of company specific vulnerabilities.

2. Control diversity: The use of technical controls, administrative controls, and physical controls
to harden security.

3. Administrative: Mandated standards set by organizational policies or other guidelines.
4. Technical: Technologies that reduce vulnerabilities, examples of this are: encryption,
antivirus software, IDSs/IPS, and firewalls.

5. User training: Providing regular training to users on common threats, emerging threats, and
social engineering in to raise awareness and help avoid attacks.

2. Given a scenario, implement secure network architecture concepts.
1. Zones/topologies:
1. DMZ: Demilitarized Zone, additional layer of protection to protect one from the internet.
2. Extranet: Private network that can only be accessed by authorized individuals. Links a
company with its suppliers and customers.

3. Intranet: Network that exclusively for the use of the members of the organizatio n, cannot be
accessed by anyone outside the organization.

4. Wireless: Generally, requires a login, an example is an internal wireless network at work.
5. Guest: Network with access to the internet but no access to the internal network. Is useful in
congested areas and is generally unsecured.

6. Honeynets: Dummy Network to attract and fool attackers.
7. NAT (Network Address Translation): Translates private IP addresses in to public and public IP
addresses to private.

8. Ad hoc: A wireless network without an access point, the connected devices communicate
directly.

2. Segregation/segmentation/isolation: Separation for performance, security, or compliance
1. Physical: Devices are separate and cannot directly communicate unless physically connected.
Does not scale well.

2. Logical (VLAN): Separate areas are segmented for different networks, but still housed on the
same switch. To connect them you need a layer 3 device, such as a router.

3. Virtualization: The hardware to separate networks is virtualized, including routers, switches,
and other devices apart from the infrastructure. Easier to manage from a security standpoint

and everything can be segmented.

4. Air gaps: Network where the devices are physically separate from another and don’t share
any components to communicate. Great for security but be careful with removable media.

3. Tunneling/VPN:
1. Site-to-site: Send data between two sites in an encrypted form. Done by installing a VPN on
both sides. Data will reach the VPN and encrypt and then the other VPN will decrypt it for the

receiving end.

2. Remote access (Host to Site): Software is installed on the device that wants the VPN tunnel,
then the encrypted tunnel is created to connect to the specific network.

4. Security device/technology placement:
## Page 18

18 | P a g e

### Skillcertpro

1. Sensors: Can give transactions, logs, or other raw data. Can be integrated or built-into
switches, servers, firewalls, routers, or other network devices.

2. Collectors: Could be a console or SIEM. Gathers all the data from sensors into one place and
attempts to make sense of it.

3. Correlation engines: Can be built in SIEM, tries to compare and correspond data collected
from the sensors to determine if an attack is present.

4. Filters: Follow the logical path, does not follow a state set of rules for traffic. Blocks harmful
traffic.

5. Proxies: Intermediary point between the client and the service. Ensures that the response
arrives safely and that the traffic flow is correct.

6. Firewalls: Is state-based so that it can filter by content and more specific perimeters. Placed
- n the outgoing and inward edges of the network.
7. VPN concentrators: Authenticates VPN clients and establishes between tunnels.
8. SSL accelerators: Offloads the SSL process to a hardware accelerator. SSL handshake is
complicated and time consuming.

9. Load balancers: Takes requests from the internet, and spreads the requests over multiple
servers, can also determine the health of servers.

10. DDoS mitigator: Sits between the network and the internet. Identifies and blocks DDOS
attacks in real time.

11. Aggregation switches:
12. Taps and port mirror: Physical tap sees what is happening in traffic packets, and software
port mirror sends a copy of the traffic packets. Is better for light traffic.

5. SDN: Aims to separate the hardware layer from the control. The network is fully virtualized with
software, and then separated into the control (configuration) and data plane (forwarding and

firewalling). Directly programmable from a central location, often automatically.

3. Given a scenario, implement secure systems design.
1. Hardware/firmware security:
1. FDE (Full Disk Encryption)/SED (Self Encryption Drives): Programs and technologies that
encrypt everything on the storage drive.

2. TPM (Trusted Platform Module): A chip on the motherboard designed to protect hardware
through integrated cryptographic keys.

3. HSM (Hardware Security Module): Accelerates cryptographic operations and manages
cryptographic keys, can be implemented as a physical device and used to accelerate RSA -

based operations.

4. UEFI (Unified Extensible Firmware Interface)/BIOS (Basic Input/Output System):
1. UEFI (Unified Extensible Firmware Interface): A method used to boot some
systems and is intended to succeed BIOS. Improves upon the BIOS design by:

allowing support for larger hard drives, having faster boot times, providing

enhanced security features, and giving the user the ability to use a mouse when

making system changes.

2. BIOS (Basic Input/Output System): Basic low-end firmware or software that
provides a computer with the basic instructions on how to start.

5. Secure boot and attestation: Processes that checks and validates system files during the boot
process.

6. Supply chain: The process of getting a product or a service from the beginning supplier to the
user.

7. Hardware root of trust: Shows that there was a secure starting point, this is proved by TPMs
having a private key burned into the hardware.

8. EMI (Electromagnetic Interference)/EMP (Electromagnetic Pulse):
## Page 19

19 | P a g e

### Skillcertpro

1. EMI (Electromagnetic Interference): Electromagnetic interferences caused by
devices that can corrupt data or prevent data from being transferred.

2. EMP (Electromagnetic Pulse): A short burst of electromagnetic energy
2. Operating systems:
1. Types:
1. Network: Supports servers, workstations, and other network-connected devices.
2. Server: Designed to function as a server.
3. Workstation: Optimized for user applications such as email and o ffice apps.
4. Appliance: A system designed to serve a purpose.
5. Kiosk: A system or computer with a touch screen designed to provide information
- r directions.
6. Mobile OS: The OS of phones, tablets, and other handheld devices.
2. Patch management: Keeping systems up to date to help improve stability and security.
3. Disabling unnecessary ports and services: Disabling unnecessary ports improves security by
preventing the users from being able to steal important data through physical storage or

injecting viruses through USB. Unnecessary services leave the system vulnerable to viruses

and exploits.

4. Least functionality: Limiting the operating system to be able to perform what is necessary.
5. Secure configurations: Changing the unsecure default setting to protect the system .
6. Trusted operating system (TOS): provides sufficient support for multilevel security and
evidence of correctness to meet high security standards.

7. Application whitelisting/blacklisting: Protects the system from potentially dangerous
applications.

1. Whitelisting: Applications allowed on the system.
2. Blacklisting: Applications blocked by the system.
8. Disable default accounts/passwords: Are easily guessable and must be changed immediately
to prevent unauthorized access.

3. Peripherals:
1. Wireless keyboards: Operate in the clear allowing for the capturing of keystrokes with a
receiver to be controlled remotely.

2. Wireless mice: Operate in the clear allowing for the capturing of movements or to be
controlled remotely.

3. Displays: Vulnerable to shoulder surfing, firmware hacks, and eavesdropping.
4. WiFi-enabled MicroSD cards: Portable storage device that has access to 802.11 Wi-Fi file
transfers.

5. Printers/MFDs (Multi-Function Devices): Reconnaissance can be performed by going through
the saved logs.

6. External storage devices: No authentication allows for anyone to read, write and move files.
7. Digital cameras: Easy to steal data.
4. Explain the importance of secure staging deployment concepts.
1. Sandboxing: Virtualizes a deployment process, allows for machines to be completely isolated from
each other, and is similar to the environment that will be used.

1. Environment: Usually tested in the actual environment that the product will be used in.
## Page 20

20 | P a g e

### Skillcertpro

2. Development: Uses a development environment, version control and change management
control to track development.

3. Test: Rigid tests are performed to find bugs and errors. Does not simulate the full product.
4. Staging: Uses data that the real product would use. Late stage testing.
5. Production: Application is now live, and the updates will be rolled out.
2. Secure baseline: Defines the core of what the development team must do. Lays out what will need to
be updated in the future.

3. Integrity measurement: Tests against the baseline to keep it secure.
5. Explain the security implications of embedded systems.
1. SCADA (Supervisory Control and Data Acquisition)/ICS (Industrial Control System): An ICS is a type of
computer-management deceive that controls industrial procedures and machines. A SCADA is a

system used over multiple industries. SCADAs can be protected with VLANs and NIPS, and they

require extensive network segmentation.

2. Smart devices/IoT (Internet of Things): A mobile device that allows the user: customizable options,
applications to help make daily activities easier, and an AI to assist in tasks. The IoT is the c lass of

devices that help provide automation and remote control of appliances and devices in the home or

- ffice.
1. Wearable technology: Contains personal and health information on a person.
2. Home automation: Technology in the home is not updated frequently and are susceptible to
attacks.

3. HVAC: Heating, ventilation, and air conditioning.
4. SoC (System on a Chip): An embedded device where the entire system is on the chip.
5. RTOS (Real Time Operating System): Attempts to use predictability to see what happens to me et real
time requirements, the guesses must be secured.

6. Printers/MFDs: Contains logs, documents, and sensitive information that can be accessed and stolen.
7. Camera systems: Videos recorders and cameras are IP devices. The risk is that they can be hacked.
8. Special purpose:
1. Medical devices: Can be attacked leaving patients at risk.
2. Vehicles: Contains onboard Wi-Fi vulnerable to threats.
3. Aircraft/UAV: Can have communications intercepted.
6. Summarize secure application development and deployment concepts.
1. Development life-cycle models:
1. Waterfall vs. Agile:
1. Waterfall: Not flexible, done in stages, and cannot go back to a previous stage
- nce the next stage is started.
2.  Agile: Flexible: allows for collaboration between groups, and can go back and fix
previous iterations.

2. Secure DevOps:
1. Security automation: Tools that automatically tests security functions, penetration, and for
vulnerabilities.

2. Continuous integration: The basic set of security checks while developing.
3. Baselining: Comparing current performance to previously set metric
## Page 21

21 | P a g e

### Skillcertpro

4. Immutable systems: Are locked and unable to change. To update the entire platform must be
updated.

5. Infrastructure as code: Turns the devices into code to allow for focusing on the application
needs instead of based on available infrastructure.

3. Version control and change management: The ability to track change and ability to revert to previous
versions.

4. Provisioning and deprovisioning: The adding and removing of assets over time. Installing new devices
and uninstalling old ones.

5. Secure coding techniques:
1. Proper error handling: Errors do not crash the system, allow for elevated privileges, or
expose private information.

2. Proper input validation: Sanitizing data to make sure it is correct and secure before using.
3. Normalization: Applying rules to a database design to ensure that the proper information
goes in the proper places.

4. Stored procedures: A program in the database that enforces the business rules.
5. Code signing: Assigning a digitally signed certificate to code.
6. Encryption: Converting readable code to unreadable garbage to make it secure.
7. Obfuscation/camouflage: Making code difficult to read.
8. Code reuse/dead code: Reusing code in multiple contexts. Code that cannot be executed.
9. Server-side vs. client-side:
1. Server-Side: Code runs on the server.
2. Client-Side: Code runs in the browser, is highly vulnerable to attacks.
6.  execution and validation:
1. Memory management: Checking and ensuring that the program does not use too much
memory.

2. Use of third-party libraries and SDKs: Commonly used so is better understood by attackers.
3. Data exposure: Disclosing private information to attackers.
7. Code quality and testing:
1. Static code analyzers: Checks source code for: conformance to coding standards, quality
metrics, and for data flow anomalies.

2. Dynamic analysis (e.g., fuzzing): Providing unexpected inputs to cause the application to
crash.

3. Stress testing: Seeing how many users a program can handle at a time.
4. Sandboxing: Using a virtual machine to run the program in a simulated environment to
determine if it will properly run. Does not affect production equipment.

5. Model verification: Ensuring the program meets specifications and performs its purpose.
8. Compiled vs. runtime code:
1. Compiled Code: Code that is optimized by an application and converted into an executable.
2. Runtime Code: The code that is interpreted as it runs.
7. Summarize cloud and virtualization concepts.
1. Hypervisor: A software, firmware or hardware that creates, manages, and operates virtual machines.
1. Type I: Known as bare metal, runs on the hardware.
2. Type II: Known as hosted, runs on top of the operating system.
## Page 22

22 | P a g e

### Skillcertpro

3. Application cells/containers: Abstracting applications from the platform into containers
allowing for applications to run without launching an entire virtual machine. This provides

portability and isolation, and less overhead than VM.

2. VM sprawl avoidance: The avoiding of a VM getting too large for the admin to properly manage. To
avoid the admin should:  enforce a strict process for deploying VMs, have a library of standard VM

images, archive or recycle under-utilized VMs, and implement a Virtual Machine Lifecycle

management Tool.

3. VM escape protection: why is this empty?
4. Cloud storage: The process of storing data in an off-site location that is leased from a provider.
5. Cloud deployment models:
1. SaaS (Software as a Service): The customer uses software that is not locally stored, instead,
all of that service is being provided in the cloud. Ex. Google docs or Gmail.

1. Everything is managed by the provider.
2. PaaS (Platform as a Service): Also known as software as a service.
3. Managed by customer: Data, applications, and making sure apps run on the OS
1. Managed by Provider: Runtime, middleware, OS, virtualization, servers, storage,
and networking.

4. IaaS (Infrastructure as a Service): Also known as hardware as a service,
1. Managed by customer: Software (applications, data, Runtime, middleware, and
- perating system).
2. Managed by Provider: Hardware (virtualization, servers, storage, and networking).
5. Private: Deployed within the organization by the organizat ion for the organization.
6. Public: Cloud is deployed by the provider within their organization for other organizations to
use.

7. Hybrid: A combination of public and private replication.
8. Community: Private or public but only shared between trusted groups.
6. On-premise vs. hosted vs. cloud:
1. On-premise: Built and managed by the company’s data center. Allows for complete control
- ver it. Has a high investment cost and operational cost.
2. Hosted: Leasing the network and storage that is off site.  Access and availability depends on
the design. Has No investment cost, and a moderate operational cost

3. Cloud: Leasing the network and storage that can be on or off site. Has no investment cost,
and a low operational cost.  Can be accessed anywhere, anytime and has high mobility.

7. VDI (Virtual Desktop Infrastructure)/VDE (Virtual Desktop Environment): The virtualization of a user's
desktop where the applications are running in the cloud or in a data center, the user runs as little of

the application as possible on the local device.

8. Cloud access security broker: Allows for the integration of security policies across all cloud -based
applications. Let’s the provider see that applications are in use and users associated with them. Can

be installed on premise or on the cloud server.

9. Security as a service (SECaaS): The provider implements their security services into your environment
via the cloud, such as: authentication anti-virus, anti-malware, IDS, and event management.

8. Explain how resiliency and automation strategies reduce risk.
## Page 23

23 | P a g e

### Skillcertpro

1. Automation/scripting:
1. Automated courses of action: Automated scripts that give a basis for secured configuration
with a secured template. Can be configured to accommodate for constant changes or can be

launched on a specific schedule.

2. Continuous monitoring: Monitors IDS/ logs, networks, SIEMs, and other systems for changes
and threats.

3. Configuration validation: Reviewing the settings of the system to ensure that its security
settings are configured correctly.

2. Templates: Gives a basis for secured configuration with a standard secured configuration.
3. Master image: Is crafted configuration of a software or entire system. Created after the target system
is installed, patched, and configured.

4. Non-persistence: Changes are possible. Due to risks of unintended changes, multiple protection and
recovery options must be established.

1. Snapshots: A copy of the live current operating environment.
2. Revert to known state: Is a recovery process that goes back to a previous snapshot.
3. Rollback to known configuration: Just a collection of settings. Does not usually include
software elements.

4. Live boot media: A portable storage device that can boot a computer. Is read -to-run or a
portable version of the OS.

5. Elasticity: The ability for the system to adapt to a workload by al locating and providing resources in an
automatic manner.

6. Scalability: The ability to handle an ever-increasing workload and able to accommodate future
growth.

7. Distributive allocation: Is providing resources across multiple services or servers as necessary instead
- f preallocation or concentrated resources based on physical system location.
8. Redundancy: Secondary or alternate solutions, it’s an alternate means to complete tasks. Helps
reduce single points of failure and boosts fault tolerance.

9. Fault tolerance: The ability for the: network, system, or computer to provide a service while
withstanding a certain level of failures. Aids in avoiding a single point of failure, a SPoF is anything that

is mission critical.

10. High availability: Refers to a system that is able to function for extended periods of time with little to
no downtime.

11. RAID (Redundant Array of Independent Disks): Is a high availability solution. Employs multiple hard
drives in a storage volume with a level of drive loss protection, except for RAID 0.

9. Explain the importance of physical security controls.
1. Lighting: If the perimeter is properly lit it can deter thieves, break-ins, and other criminal activity.
2. Signs: Allows for controlled entry point, is a psychological deterrent, and helps new and visitors find
their way. Informs of security cameras, safety warnings, and that an area is restricted.

3. Fencing/gate/cage: A fence sets the boundaries of the property and protects against casual intruders.
Gates allow for controlled entry and exit. Cages protect assets from being accessed by unauthorized

individuals.

4. Security guards: Humans are adaptable, can adjust to live events, and can react to real time intrusion
events. Can intervene and control the security devices.

5. Alarms: Notify security personnel and the authorities of unauthorized activities.
6. Safe: Protects valuables from thieves and natural disasters.
7. Secure cabinets/enclosures: Restricts unauthorized personnel from accessing cabinets.
8. Protected distribution/Protected cabling: Is a standard on how  to safely transmit unencrypted data.
Protects from wire-taps.

9. Airgap: Ensure secure networks are physically isolated from unsecure networks.
## Page 24

24 | P a g e

### Skillcertpro

10. Mantrap: Area between two doorways to identify and authenticate individuals.
11. Faraday cage: Metal screen to protect equipment from electrostatic and electromagnetic influences.
12. Lock types: Can use a key, key-pad, cards, or biometrics.
13. Biometrics: Uses physical characters to identify the individual.
14. Barricades/bollards: Stops and guides traffic, it can also prevent the entrance of vehicles.
15. Tokens/cards: Items necessary to gain access to secured areas of the building. Can contain
information that can identify and authorize an individual.

16. Environmental controls:
1. HVAC: Keeps servers from overheating and shutting down.
2. Hot and cold aisles: Allows for air flow control and for the air to move through the data
center strategically.

3. Fire suppression: Protects the equipment from fire, smoke, corrosion, heat, and water
damage. Early fire detection is vital for protecting personal and equipment from harm.

17. Cable locks: Protects small equipment from theft.
18. Screen filters: Reduces the range of visibility to prevent shoulder suffering.
19. Cameras: Deters criminal activity and creates a record of events.
20. Motion detection: Senses movement and sound in a specific area.
21. Logs: Document visitor access, allows for the identifying and record keeping of everyone who has
access to the premise.

22. Infrared detection: Detects and monitors changes in the temperature.
23. Key management: Ensure only authorized individuals only have access to the areas they need to
complete their work

4.0 Identity and Access Management
1. Compare and contrast identity and access management concepts
1. Identification, authentication, authorization and accounting (AAA):
1. Identification: Finding the unique individual on the system.
2. Authentication: The ability to tell if an individual is actually who they claim they are.
3. Authorization: Determining what an individual can and cannot access on a system.
4. Accounting: The tracking of an individual’s actions on the system.
2. Multifactor authentication: Uses at least two of the factors of authentication.
1. Something you are
2. Something you have
3. Something you know
4. Somewhere you are
5. Something you do
3. Federation: The authenticating and authorizing between two parties. Ex. Logging onto Facebook with
Google account.

4. Single sign-on: Only uses one of the factors of authentication.
5. Transitive trust: There are more than two entities, one entity is trusted because they are trusted by
someone the company trusts.

2. Given a scenario, install and configure identity and access services.
1. LDAP (Lightweight Directory Access Protocol):
## Page 25

25 | P a g e

### Skillcertpro

Queries information about the directory. Is a hierarchical structure; CN = Common Name, OU = Organizational

Unit, DC = Domain Controller. Utilizes TCP/IP, TCP/UDP ports 389.

6. Secure LDAP: LDAP over SSL/TLS, uses TCP on port 636. Does not send queries in plain text.
2. Kerberos: Developed by MIT, for mutual authorization between client and server. It uses a ticket
granting system for authorization. Is a government standard.

3. TACACS+ (Terminal Access Controller Access Control System): Runs TCP over port 49, encrypts all
parts of communication. Does not suffer due to security issues caused by RADIUS. Authorization and

Authentication are separated for granular control.

4. CHAP (Challenge Handshake Authentication Protocol): Authenticates PPP clients to the server. Uses a
- ne-way hash based on a shared secret that is compared on the client and server end. Does not send
plaintext over the wire.

5. PAP (Password Authentication Protocol): Username and password are sent as plaintext and are no
longer used.

6. MS-CHAP (Microsoft CHAP): Delivers a two-way, mutual authentication between the server and
client. Separate keys are created for sent and received data. Is seen as weak due to it using a 5-bit

encryption system, same as NTLM.

7. RADIUS (Remote Authentication and Dial-in User service): Combines authentication and
authorization, only encrypts the passwords, each network device must contain an authorization

configuration. There is no command logging, and minimal vendor support. Uses ports 1812 for

authentication and authorization and port 1813 for accounting functions.

8. SAML (Security Association Markup Language): Authenticates through a third -party source to gain
access, the resource is not responsible for the authentication. The request is passed through a trusted

third-party server.

1. The three roles are: Principle (the user or client), identity provider (the one who assures the
identity of the principle), and service provider (a web service of some type.)

9. OpenID Connect: OpenID Connect handles the authentication part of the identification process and
uses OAuth for authorization.

10. OAUTH (Open Standard for Authorization): Token authorization happens in the back ground. Uses a
logon from a larger trusted service.

11. Shibboleth: An open-source software that uses SAML to provide a third-party federated SSO
authentication.

12. Secure token: An authentication mechanism that can be used to identify and authenticate, and to
deny and allow access.

13. NTLM (New Technology LAN Manager): Used for authenticating in a Windows domain, was replaced
by Kerberos for the most part.

1. NTMLv2: Is the most common form used, is somewhat insecure.
3. Given a scenario, implement identity and access management controls.
1. Access control models:
1. MAC (Mandatory Access Control): Based on classification rules. Objects are given sensitivity
labels, subjects given clearance labels, and users obtain access by having the correct

clearance. The classifications are hierarchical.

2. DAC (Discretionary Access Control): Is based on user identity. Users are granted access
through ACLs placed on objects through the object’s owner or creator.

1. ACL (Access Control List): A security logical device attached to all objects and
resources, it defines which users are granted or denied access.

## Page 26

26 | P a g e

### Skillcertpro

3. ABAC (Attribute Based Access Control): Assigning access and privileges through a scheme of
attributes. Relations and criteria determine access; time of day, location, and/or IP address.

4. Role-based access control: Access is based on the job and position of the user.
Changing permissions of a group changes the permissions for all of the members. Not good

for companies with high turn-over rates.

5. Rule-based access control: Rules are created by the admin to monitor usage and if a user
needs access they must meet the requirements of the rules. Rules are enforced regardless of

the user.

2. Physical access control:
1. Proximity cards: A smart card that does not require direct contact.
2. Smart cards: Cards that contain identification/authentication information in an integrated
circuit chip. Often uses dual factor authentication; something you have (the card),  and

something you know (a pin or password).

3. Biometric factors: Verifies identity through physical features.
1. Fingerprint scanner: Scans the unique patterns of the fingerprint to grant access.
2. Retinal scanner: Blood vessels in the back of the retina.
3. Iris scanner: Scans the Iris.
4. Voice recognition: The identification and translation of spoken language for authorization of
a user. Is vulnerable to impersonation.

5. Facial recognition: The identification of an individual from a digital image or a video frame. Is
vulnerable to impersonation.

6. False acceptance rate (FAR): Incorrectly identifies an unauthorized user as a n authorized
user. Type 2 error.

7. False rejection rate (FRR): Incorrectly identifies an authorized user as an unauthorized user.
Type 1 error.

8. Crossover error rate (CER): The point on a graph where the FAR and FRR meet. The lowest
CER point is the most accurate biometric device for a body part.

4. Tokens
1. Hardware:  A device that displays and constantly generates a pin or password.
2. Software: An app or software that generates a token.
3. HOTP/TOTP: Open source standards to generate one-time use passwords.
1. HOTP (HMAC-based One-Time Password):  Can be used only once before it
expires.

2. TOTP (Time-based One-time Password): Only last for around 30 seconds before it
expires.

5. Certificate-based authentication:
1. PIV/CAC/smart card: Cards that have embedded certificates and a photo ID for
authorization. The US DOD uses CAC/PIV.

2. PIV (Personal identity verification): Is for civilians working for the federal
government.

3. CAC (Common access card): Is for Department of Defense members.
4. IEEE 802.1x: Offers port-based authentication to wireless and wired networks to prevent
rogue devices from connecting to secured ports.

## Page 27

27 | P a g e

### Skillcertpro

6. File system security: The means of ensuring that files are encrypted and can  only be used by properly
authorized users have access to them or modify them.

7. Database security: MS and Oracle allow for the DB to be encrypted.
4. Given a scenario, differentiate common account management practices.
1. Account types:
1. User account: An account that is a collection of information that identifies an individual and
grants them specific areas of the network or system.

2. Shared and generic: Multiple individuals sign into a single account. No workplace should have
these, cannot distinguish the actions of the user.

2. accounts/credentials:
1. Guest accounts: An anonymous shared logon account.
2. Service accounts: Performs specific maintenance actions, such as a backup, account and
server operators.

3. Privileged accounts: Access is set to access rights, generally referred to as system or network
administrative accounts.

3. General Concepts:
1. Least privilege: Rights and permission are set to bare minimum.
2. Onboarding/offboarding:
1. Onboarding: Helps new employees learn all of the facets of their new job.
2. Offboarding: Helps leaving employees learn how to properly leave and potentially
return to the company.

3. Permission auditing and review:
4. Usage auditing and review:
5. Time-of-day restrictions: Certain privileges are permitted or restricted based on the time of
day.

6. Recertification: The action of regaining a certification due to the certification being expired.
7. Standard naming convention: Allows for the easier identification of resource location and
purpose. Reduces the amount of time needed for troubleshooting and training.

8. Account maintenance: Making sure that accounts have the proper privileges, and unused
accounts are deleted. Generally done through scripts to save time and money.

9. Group-based access control: Every user in a group has the same privileges.
10. Location-based policies: Grants and denies access based on the user’s location.
11. Account policy enforcement:
12. Credential management: Stores, manages, and tracks user credentials.
13. Group policy: Sets different privileges of the system and allows for these to be managed or
set those across entire groups or even through the entire network and every computer

within it.

14. Password complexity: The enforcing of complex and difficult to guess passwords.
15. Expiration: The amount of time that passes before a password is required to be changed.
16. Recovery: The ability to find lost passwords and usernames in case an employee forgets
them.

17. Disablement: Disabling an account.
18. Lockout: Prevents login from specific individual after a set of failed login attempts, for a set
period of time.

19. Password history: Remembers past passwords and prevents the reuse of passwords.
20. Password reuse: The ability to ever use the same password again.
## Page 28

28 | P a g e

### Skillcertpro

21. Password length: The minimum amount of characters that can be used in a password.
22. Password age: A policy that sets how long a user can have a password before they are forced
to change it.

6.0 Cryptography and PKI
1. Compare and contrast basic concepts of cryptography.
1. Symmetric algorithms: A shared secret key used by the sender and receiver to encrypt and decrypt.
2. Modes of operation:
3. Asymmetric algorithms: There is a shared public key and a private secret key. Public  key encrypts and
the private key decrypts, private key to sign and public key verify.

4. Hashing: An algorithm that creates a unique one-way encryption, not plaintext.
5. Salt, IV, nonce:
1. Salt: The adding of input to random data to function to make it more comp licated. A small
piece of data added to the end of a password when creating a hash

2. IV (Initialization Vector): A random value used with an encryption key.
3. Nonce: One-time use random value used for authentication.
6. Elliptic curve (ECC): Great for low powered machines. Uses curves for encryption instead of large
prime numbers.

7. Weak/deprecated algorithms: Weak due to vulnerabilities (WEP) or weak key length (DES is on 56 -
bits) which is easy to brute force through.

8. Key exchange: Securely sending keys back and forth. Out-of-Band where the key is sent over the
phone, in person, or any other way offline. In-Band is sent over the internet encrypted.

9. Digital signatures: Provides integrity, verifies that the original sender is actually the one who sent it.
This can be done through asymmetric encryption, where there is a hash message then they will

encrypt the hash using their private key, creating a digital signature that can only originate from

them. To verify, the signature is decrypted with the public key, and the me ssage is then hashed. If the

two hashes match, then the digital signature is valid

10. Diffusion: Changing one character causes the plaintext to drastically change the outputted cipher.
11. Confusion: The cipher doesn’t look anything like the plain text.
12. Collision: Two completely different pieces of data have the exact same hash.
13. Steganography: Hides messages or code inside of an image or another type of data. Impossible to
decipher without the correct tools.

14. Obfuscation: Taking something and making it difficult for a human to understand, however it is not
impossible to convert it back to the original form.

15. Stream vs. block:
16. Key strength: Larger keys and more bits are signs of better encryption and stronger keys.
17. Session keys: Symmetric keys used to provide a secure and fast online connection. The server’s public
key is paired with a random key to produce a symmetric key, that the server uses to encrypt and the

user to decrypt.

18. Ephemeral key: Session keys that only last temporarily and change frequently.
19. Secret algorithm: Is a symmetric encryption. Uses the same key for the sender to encrypt and the
receiver to decrypt.

20. Data-in-transit: Data being transmitted over a network. Should be encrypted using TLS and IPSec.
21. Data-at-rest: Data in a storage device.
22. Data-in-use: Data being ran through RAM or CPU, is almost always decrypted to make it easier to use.
23. Random/pseudo-random:
1. Number generation: Used to create random keys and salts, a computer is never truly
random, so it relies on outside factors such as user input to create a more random number.

## Page 29

29 | P a g e

### Skillcertpro

24. Key stretching: Hashing a password, and then hashing that hashed value. Protects a weak password
from brute force attacks.

25. Implementation vs. algorithm selection:
1. Crypto service provider: A library of cryptographic standards and algorithms.
2. Crypto modules: Hardware, firmware or software that provides the hash, HMAC, cipher,
decipher, sign, and verify methods.

26. Perfect forward secrecy (PFS): Prevents point of failure where a stolen private key can decrypt all
connections by generating a new key each session. Protects past sessions against future compromises

- f secret keys.
27. Security through obscurity: Relying on secrecy to protect and secure data.
28. Common use cases:
1. Low power devices: Mobile phones and portable devices.
2. Low latency: Low amount of time occurs between input and output.
3. High resiliency: Larger key sizes and encryption algorithm quality.
4. Supporting confidentiality: Secrecy and privacy.
5. Supporting integrity: Preventing modification of data and validating contents with hashes.
6. Supporting obfuscation:
7. Supporting authentication: Password hashing and protecting the original password.
8. Supporting non-repudiation: Digital signature provides: authenticity, integrity, and non -
repudiation.

9. Resource vs. security constraints: Limitations in providing strong cryptography due to the
amount of available resources (time and energy) vs the security provided by cryptography.

2. Explain cryptography algorithms and their basic characteristics.
1. Symmetric algorithms:
1. AES (Advanced Encryption Standard): Symmetric, block cipher with 128-bit blocks, key sizes
- f 128-bit, 192-bit and 256-bit. It utilizes the Rijndael algorithm and is the U.S. government
standard for the secure exchange of sensitive but unclassified data. It is also the encryptio n

standard used today with WPA2.

2. DES (Data Encryption Standard): Symmetric, was common until replaced by AES, the block
cipher is 64-bit and the key is 56-bit (very small), this means it can easily be brute forced.

3. 3DES: Symmetric, very secure and upgrade over DES with three separate keys and three
passes over data. Not used in modern day either.

4. RC4: Symmetric, part of the original WEP standard with SSL, removed from TLS, key sizes of
40-bit to 2048-bit. Deprecated from biased output.

5. Blowfish/Twofish:
1. Blowfish: Symmetric, fast and has variable key-lengths from 1-bit to 448-bits, uses
64-bit block cipher. Not limited by patents.

2. Twofish: Symmetric, uses a very complex key structure up to 256-bits but still
similar to predecessor, works using 128-bit blocks. Again, not limited by patents.

2. Cipher modes:
1. CBC (Cipher Block Chaining): Symmetric, uses IV for randomization. Encryption that is
dependent on the block before it. Slow.

2. GCM (Galois Counter Mode): Used by many. Provides data authenticity/integrity, ha shes as
well. Widely used.

3. ECB (Electronic Code Book): Mode of operation, simplest cipher mode, not recommended.
4. CTR (Counter Mode): Converts block into stream, uses IV. Widely used.
## Page 30

30 | P a g e

### Skillcertpro

5. Stream vs. block:
3. Asymmetric algorithms:
1. RSA (Rivest, Shamir, Adleman): First practical use of public key cryptography, uses large
prime numbers as the basis for encryption.

2. DSA (Digital Signature Algorithm): Standard for digital signatures and modifies Diffie -
Hellman, follows usage of elliptic curves to create ECDSA.

3. Diffie-Hellman: An asymmetric standard for exchanging keys. Primarily used to send private
keys over public (unsecured) networks.

1. Groups: Diffie-Hellman (DH) groups determine the strength of the key used in the
key exchange process. Higher group numbers are more secure, but require

additional time to compute the key.

2. DHE (Diffie-Hellman Ephemeral): A Diffie-Hellman key exchange that uses
different keys.

3. ECDHE (Elliptic Curve Diffie-Hellman Ephemeral): Key agreement protocol that
allows 2 parties, each having an elliptic curve public-private key pair, to establish

a shared secret over an insecure channel.

4. Elliptic curve cryptography (ECC): Asymmetric, uses smaller key sizes and curve algorithms to
secure data, useful in portable devices because it uses less CPU power.

5. PGP (Pretty Good Privacy)/GPG (GNU Privacy Guard):
1. PGP (Pretty Good Privacy): Asymmetric, used by many for emails and is used by
IDEA algorithm.

2. GPG (GNU Privacy Guard): A free, open-source version of PGP that provides
equivalent encryption and authentication services.

4. Hashing algorithms: Hashing provides integrity and authenticity.
1. MD5 (Message-Digest Algorithm v5): Hashing algorithm, 128-bit hash with strong security,
collision was found in 1996 so it is not used as much nowadays.

2. SHA (Secure Hash Algorithm): Hashing algorithm, one-way 160-bit hash value with
encryption protocol. Standard hash algorithm today, went from SHA-1 (160-bit digest,

deprecated) to SHA-2 (512-bit digest, still used).

3. HMAC (Hash-Based Message Authentication Code): Hashing algorithm that combines itself
with a symmetric key. Provides data integrity as well as authenticity, but is faster than

asymmetric encryption.

4. RIPEMD (RACE Integrity Primitives Evaluation Message Digest): Hashing algorithm that is
based on MD4, collisions were found so it now exists in versions of 160-bits, 256-bits, and

320-bits.

5. Key stretching algorithms: Lengthen key to make brute-force attacks harder.
1. Bcrypt: Key Stretching that helps protect passwords by repeating Blowfish cipher.
2. PBKDF2 (Password-Based Key Derivation Function 2): Key Stretching, applies RSA function to
password to create stronger key.

6. Obfuscation: Making something unclear to read, but can still reverse it.
1. XOR (Exclusive OR): Mathematical operation that's a part of all symmetric operations, done
by comparing bits of plaintext and a key (same=0, different=1). Can be reversed to get

plaintext back.

2. ROT13 (Rotate by 13): Common substitution cipher, rotates each letter 13 places.
## Page 31

31 | P a g e

### Skillcertpro

3. Substitution ciphers: Cipher that changes one symbol for another, like the Caesar Cipher.
Easy to decrypt.

3. Given a scenario, install and configure wireless security settings.
1. Cryptographic protocols:
1. WPA (Wi-Fi Protected Access): Uses RC4 with TKIP. Was replaced by WPA2.
2. WPA2 (Wi-Fi Protected Access v2): Uses CCMP for encryption.
3. CCMP (Counter Mode with Cipher Block Chaining Message Authentication Code Protocol): Is
based on 128-bit AES is more secure than TKIP. Was advanced for its time.

4. TKIP (Temporal Key Integrity Protocol): Protocol that mixes a root key wi th an initialization
vector, a new key for each packet.

2. Authentication protocols:
1. EAP (Extensible Authentication Protocol): Is an authentication framework that provides
general guidance for authentication methods.

2. PEAP (Protected Extensible Authentication Protocol): An extension of EAP that is sometimes
used with 802.1x, a certificate is required on the 802.1x server.

3. EAP-FAST (EAP Flexible Authentication with Secure Tunneling): A Cisco-designed replacement
for Lightweight EAP, supports certificates but are not required.

4. EAP-TLS (EAP Transport Layer Security): This is one of the most secure EAP standards and is
widely implemented on many networks. It uses PKI, so certificates are required on the 802.1x

server and on the clients.

5. EAP-TTLS (EAP Tunneled Transport Layer Security): Allows for systems to use older
authentication methods such as PAP within a TLS tunnel. Certificate is required on the 802.1x

server but not on the clients.

6. IEEE 802.1x: An authentication protocol used in VPNs, wired and wireless  networks. In VPNs
it is used as a RADIUS server, wired use it as a port-based authentication, and wireless use it

in Enterprise mode. Can be used with certificate-based authentication.

7. RADIUS Federation: Members of one organization can authenticate to the  network of
another network using their normal credentials.

3. Methods:
1. PSK vs. Enterprise vs. Open:
1. PSK (Pre-Shared Key): Uses WPA2 encryption along with a key that everyone
needs to know to access the network.

2. Enterprise: Users to authenticate using a username and password, and uses
802.1X to provide authentication, server handles distribution of keys/certificates.
3. Open: Does not apply any security.
2. WPS: Allows users to easily configure a wireless network, often by using only a PIN. Are
susceptible to brute force attacks because they can discover the PIN.

3. Captive portals: Forces clients using a web browser to complete a task before being able to
access the network.

4. Given a scenario, implement public key infrastructure.
1. Components:
## Page 32

32 | P a g e

### Skillcertpro

1. CA (Certificate Authority): A trusted third-party agency that is responsible for issuing digital
certificates.

2. Intermediate CA (Intermediate Certificate Authority): An entity that processes the CSR and
verifies the authenticity of the user on behalf of a CA.

3. CRL (Certificate Revocation List): A list of certificates that are: no longer valid, expired, or that
have been revoked by the issuer.

4. OCSP (Online Certificate Status Protocol): A request and response protocol that obtains the
serial number of the certificate that is being validated and reviews revocation lists for the

client.

5. CSR (Certificate Signing Request): A user request for a digital certificate
6. Certificate: Digitally signed statement that associates a public key to the corresponding
private key.

7. Public key: A key that is provided by the sender, used by anyone to encrypt with asymmetric.
8. Private key: Key used to decrypt a message, only used by the person opening the message.
9. Object identifiers (OID): A serial number that authenticates a certificate.
2. Concepts:
1. Online vs. offline CA:
1. Online CA: Is directly connected to a network, most common.
2. Offline CA: Is not directly connected to a network, often used for root certificates.
2. Stapling: Combining related items in order to reduce communication steps. The device that
holds the certificate will also be the one to provide status of any revocation.

3. Pinning: The application has hard-coded the server’s certificate into the application itself.
4. Trust model: A complex structure of: systems, personnel, applications, protocols,
technologies, and policies working together to provide protection.

5. Key escrow: Private keys are kept by the users and a 3rd party as back -ups.
6. Certificate chaining: Certificates are handled by a chain of trust, the trust anchor for the
digital cert is the root CA.

3. Types of certificates:
1. Wildcard: A Certificate that can be used with multiple subdomains of a given domain, by
covering the all subordinate certificates to the root.

2. SAN (Subject Alternative Name): The certificate has several uses, allows a certificate to be
valid for multiple domains using multiple names.

3. Code signing: Digitally signs written application code and makes sure that it adheres to policy
restriction and usage.

4. Self-signed: The root CA creates its own certificate.
5. Machine/computer: Certificates that are assigned to a specific machine.
6. Email: Secures emails, is used by S/MIME.
7. User: Often for authentication or to access resources.
8. Root: Used for root authorities, they usually are self-signed.
9. Domain validation: Provides a secure communication with a specific domain
and provides TLS, this is the most common form of certificate.

10. Extended validation: Are more secure because they require more validation from the
certification holder.

4. Certificate formats:
1. DER (Distinguished Encoding Rules): Are common and designed for X.509 certificates, they
are used to extend binary encoded certificates. Cannot be edited by a plain text editor. Used

with java commonly.

## Page 33

33 | P a g e

### Skillcertpro

2. PEM (Privacy Enhanced Mail): Most common format in which certificates are issued. Multiple
certificates and the private key can be included in one file. The file is encoded ASCII. PEM file

extensions include .pem, .crt, .cer, and .key. Apache servers typically use PEM -format files.

3. PFX: A precursor to P12, has the same usage. Administrators often use this to  format on
Windows to import and export certificates.

4. CER (Certificate File): May be encoded as binary DER or as ASCII PEM.
5. P12: Is a PFX extension used in windows
1. PKS 12 (Public Key Cryptography Standards #12): Is part of the RFC standard.
Stores many types of certificates and can be password protected.

2. RFC (Remote Function Call): A formal document describes the specifications for a
particular technology, was drafted by the Internet Engineering Task Force.

6. P7B: Is stored in Base64 ASCII, containing certificates and chains but not the private key.