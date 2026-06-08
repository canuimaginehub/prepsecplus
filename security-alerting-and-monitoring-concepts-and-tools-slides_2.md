# security-alerting-and-monitoring-concepts-and-tools-slides_2

## Page 3

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
## Page 4

- 
- 
- 
- 
## Page 5

- 
- 
- 
- 
## Page 6

- 
- 
- 
- 
## Page 7

- 
- 
- 
- 
## Page 11

- 
- 
- 
- 
- 
- 
- 
- 
## Page 12

- 
- 
- 
- 
## Page 14

- 
- 
- 
- 
## Page 18

<?xml version="1.0" encoding="UTF-8"?>

<arf:AssetReport

xmlns:arf="http://scap.nist.gov/schema/asset-report/0.1"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://scap.nist.gov/schema/asset-

report/0.1

http://scap.nist.gov/schema/asset-

report/0.1/asset-report_0.1.xsd">

<arf:ReportHost id="example-host-1">

<arf:HostName>example.com</arf:HostName>

<arf:OperatingSystem>

<arf:Name>Windows Server 2019</arf:Name>

</arf:OperatingSystem>

<arf:IPAddress>192.168.1.100</arf:IPAddress>

<arf:AssetIdentifiers>

<arf:CPE>CPE-

2.3:2.3:o:microsoft:windows_server:2019:*:*:*:*:*:*</arf
### :Cpe>

</arf:AssetIdentifiers>

<arf:Vulnerabilities>

<arf:Vulnerability id="CVE-2022-1234">

<arf:Severity>High</arf:Severity>

<arf:CVE>CVE-2022-1234</arf:CVE>

<arf:Description>A description of the

vulnerability.</arf:Description>

<!-- Additional vulnerability information -->

</arf:Vulnerability>

<!-- Additional vulnerabilities for this host -->

</arf:Vulnerabilities>

<arf:Compliance>

<arf:Policy id="example-policy-1">

<arf:Title>Organization Security

Policy</arf:Title>

<arf:Status>Pass</arf:Status>

<!-- Additional compliance information -->

</arf:Policy>

<!-- Additional compliance policies for this host

- >
</arf:Compliance>

</arf:ReportHost>

<!-- Additional report hosts -->

</arf:AssetReport>

## Page 19

- Data aggregation
- Correlation
- Automated alerting and triggers
- Time synchronization
- Event deduplication
- Logs/WORM
## Page 24

- 
- 
- 
## Page 26

- 
- 
- 
- 
## Page 29

- Source and destination IP address
- IP protocol field value
- Source and destination port numbers
- Counters (packets, bytes)
- Timestamps (start and end time)
- Where observed (interface and direction
(ingress/egress))

- Unidirectional or bidirectional
## Page 31

- Collector export protocol (based on NetFlow v9)
- Non-proprietary
- Packet count, byte count, type of service, flow
direction, routing domain, etc.

- Network monitoring/measurement,
accounting/billing

## Page 34

- 
- 
- 
- 