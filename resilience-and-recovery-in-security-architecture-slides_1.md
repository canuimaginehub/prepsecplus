# resilience-and-recovery-in-security-architecture-slides_1

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
## Page 7

- 
- 
## Page 8

- 
- 
- 
- 
## Page 9

- 
- 
- 
- 
## Page 10

- 
- 
- 
- 
## Page 11

- 
- 
- 
- 
## Page 14

Type of Site Pros

Type of Site Cost

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
## Page 15

### Wa

### Or

### Ca

### Mt

### Id

### Nv

### Az

### Ut

### Wy

### Co

### Nm

### Tx

### Ok

### Ks

### Ne

### Sd

### Nd

### Mn

### Ia

### Mo

### Ar

### La

### Ms

### Al

### Ga

### Fl

### Sc

### Tn

### Nc

### Il

### Wi Mi

### Oh

### In

### Ky

### Wv Va

### Pa

### Ny

### Me

### Vt

### Nh

### Nj

### De

### Md

Washington D.C.

### Ma

### Ct

### Ri

### Ak

### Hi

## Page 16

### Wa

### Or

### Ca

### Mt

### Id

### Nv

### Az

### Ut

### Wy

### Co

### Nm

### Tx

### Ok

### Ks

### Ne

### Sd

### Nd

### Mn

### Ia

### Mo

### Ar

### La

### Ms

### Al

### Ga

### Fl

### Sc

### Tn

### Nc

### Il

### Wi Mi

### Oh

### In

### Ky

### Wv Va

### Pa

### Ny

### Me

### Vt

### Nh

### Nj

### De

### Md

Washington D.C.

### Ma

### Ct

### Ri

### Ak

### Hi

## Page 17

### Wa

### Or

### Ca

### Mt

### Id

### Nv

### Az

### Ut

### Wy

### Co

### Nm

### Tx

### Ok

### Ks

### Ne

### Sd

### Nd

### Mn

### Ia

### Mo

### Ar

### La

### Ms

### Al

### Ga

### Fl

### Sc

### Tn

### Nc

### Il

### Wi Mi

### Oh

### In

### Ky

### Wv Va

### Pa

### Ny

### Me

### Vt

### Nh

### Nj

### De

### Md

Washington D.C.

### Ma

### Ct

### Ri

### Ak

### Hi

## Page 19

- 
- 
## Page 20

- 
- 
- 
## Page 26

- 
- 
- 
- 
## Page 27

- 
- 
- 
- 
## Page 28

- 
- 
- 
- 
- 
## Page 29

- 
- 
- 
## Page 30

- 
- 
- 
- 
- 
- 
- 
## Page 31

- 
- 
- 
- 
## Page 35

- 
- 
- 
## Page 36

- 
- 
- 
## Page 37

- 
- 
- 
## Page 38

- 
- 
- 
## Page 39

- 
- 
- 
## Page 40

- 
- 
- 
- 
- 
- 
- 
- 
## Page 41

- 
- 
- 
- 
- 
- 
## Page 44

- 
- 
- 
- 
- 
## Page 45

- 
- 
- 
- 
## Page 46

Define what network, storage and compute components make up the

application or service

Typically more than one team manages the various components of an

application or service.  Ensure they are all aware and represented

Test backup and restoration of the application or service before a crisis occurs

to ensure the required data is actually available

## Page 47

Data that has changed since the last full backup.  The time to backup increases over time, but the time to restore

is reduced only requiring two backup media

Data that has changed since the last incremental backup.  Time to backup is reduced, but time to restore is

increased as all incremental backups plus last full back is required

All data is backup up each time

Point in time copy of the data, that typically maintains pointers to the original data rather than copying the data

itself.  Snapshots can be performed very quickly

## Page 49

Network Attached Storage

Storage Area Network

Replicate to another

NAS device

Replicate to another

SAN array

## Page 51

Backups can be geographically far away to be asynchronous vs. high-

availability (HA) requires synchronous speeds

How long would it take to get tapes back in the event of disaster?

Hot, warm or cold site, time required to recover offsite backups, order of

recovery, app consistent/crash consistent

## Page 52

Prevents people from customizing their desktops, installing unapproved

applications, tweaking settings, etc.

Allows a user to quickly revert to a known good state or rollback changes in

the event a virus, malware, spyware is installed

Operating system on USB drive or removable media to allow cleaning of a system, removing

malware, etc.

## Page 53

Battery backup that provides power in the event of a disruption (sag, outage,

etc.)  Length of time depends on type of UPS, batteries, etc.

Alternate power supply that typically runs on gas, and turns on if power

dip/outage is detected

Power is supplied by dual feeds independent of one another (A side and B side)

Provides the ability to monitor and control critical factors such as voltage,

current and power factor
