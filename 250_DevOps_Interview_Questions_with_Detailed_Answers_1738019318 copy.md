# 250_DevOps_Interview_Questions_with_Detailed_Answers_1738019318 copy

## Page 1

DevOps  Shack          250  Linux  Scenario  Based  Interview                     Questions  and  Answers

Q1:  How  would  you  find  all  files  larger  than  100MB  in  a  directory  and  its

subdirectories?

Answer:  Use  the  find command:

find  /path/to/directory  -type  f  -size  +100M

○  -type  f:  Finds  only  files.  ○  -size  +100M:  Specifies  files  larger  than  100MB.

Q2:  What  does  the  command  chmod  755  file do?

●  Answer:  ○  Changes  the  file's  permissions  to  755.  ○  7:  Full  permission  for  the  owner  (read,  write,  execute).  ○  5:  Read  and  execute  for  group  and  others.

Syntax  breakdown:

r  =  4,  w  =  2,  x  =  1  →  rwx  (7),  r-x  (5)

Q3:  How  do  you  recursively  delete  all  .log files  in  a  directory?

Answer:

## Page 2

find  /path/to/directory  -name  "*.log"  -type  f  -delete

○  -name  "*.log":  Matches  files  with  .log extension.  ○  -type  f:  Targets  only  files.  ○  -delete:  Deletes  the  files  found.

Q4:  How  do  you  create  a  tarball  of  /var/log and  compress  it  with  gzip?

Answer:

tar  -czvf  logs.tar.gz  /var/log

○  -c:  Creates  a  tarball.  ○  -z:  Compresses  using  gzip.  ○  -v:  Verbose  output.  ○  -f  logs.tar.gz:  Specifies  the  tarball  file  name.

Q5:  How  do  you  troubleshoot  a  network  issue  where  a  server  is  unreachable?

●  Answer:

Check  network  connectivity:

ping  <server_ip>   Verify  DNS  resolution:

nslookup  <server_name>   Check  routes:

ip  route

## Page 3

Verify  firewall  settings:

sudo  iptables  -L   Test  specific  port  availability:

nc  -zv  <server_ip>  <port>

Q6:  How  do  you  permanently  assign  an  IP  address  in  Linux?

●  Answer:  Edit  the  network  configuration  file:

For  RHEL/CentOS:

vi  /etc/sysconfig/network-scripts/ifcfg-eth0

Add  or  update:

IPADDR=192.168.1.100  NETMASK=255.255.255.0  GATEWAY=192.168.1.1   Restart  the  network  service:

sudo  systemctl  restart  network

Q7:

How

do

you

identify

a

process

consuming

high

CPU?

Answer:

○  Sort  by  CPU  usage  by  pressing  Shift  +  P.

## Page 4

Alternatively,  use:

ps  -eo  pid,ppid,cmd,%mem,%cpu  --sort=-%cpu  |  head

Q8:  How  do  you  monitor  disk  I/O  in  real-time?

Answer:  iostat  -x  2

○  -x:  Shows  extended  statistics.  ○  2:  Refreshes  every  2  seconds.

Q9:  How  do  you  kill  a  process  by  its  name?

Answer:

pkill  <process_name>   To  verify:

pgrep  <process_name>

Q10:  How  do  you  list  all  services  and  their  statuses?

Answer:

systemctl  list-units  --type=service

Q11:  How  do  you  set  up  a  basic  firewall  rule  to  allow  SSH  traffic?

Answer:

sudo  ufw  allow  ssh

## Page 5

Check  the  status:

sudo  ufw  status

Q12:  How  do  you  check  for  unauthorized  access  attempts  on  your  server?

Answer:

sudo  cat  /var/log/auth.log  |  grep  "Failed  password"

Q13:  Write  a  script  to  check  if  a  file  exists  and  display  its  permissions.

Answer:

#!/bin/  FILE=$1  if  [  -e  "$FILE"  ];  then      echo  "File  exists."      ls  -l  "$FILE"  |  awk  '{print  $1}'  else      echo  "File  does  not  exist."  fi

○  Usage:  ./script.sh  filename

Q14:  How  would  you  write  a  script  to  archive  logs  older  than  7  days?

Answer:

#!/bin/  find  /var/log  -type  f  -mtime  +7  -exec  tar  -rvf  old_logs.tar

{}

\;

- exec
rm

{}

\;

## Page 6

○  -mtime  +7:  Finds  files  older  than  7  days.  ○  -exec:  Executes  tar to  archive  and  rm to  delete.

Q15:  How  do  you  add  a  new  user  with  a  specific  home  directory?

Answer:  sudo  useradd  -m  -d  /custom/home/username  username

○  -m:  Creates  the  home  directory.  ○  -d:  Specifies  the  custom  directory.

Q16:  How  do  you  change  the  default  shell  for  a  user?

Answer:

sudo  usermod  -s  /bin/  username   Verify  with:

cat  /etc/passwd  |  grep  username

Q17:  What  steps  would  you  take  to  troubleshoot  a  slow  server?

●  Answer:

Check  CPU  usage:

Top   Analyze  disk  usage:

df  -h

## Page 7

Inspect  running  processes:

ps  aux  --sort=-%cpu  |  head   Check  I/O  operations:

iostat  -x  2   Verify  memory  usage:

free  -m

Q18:  How  do  you  resolve  a  "permission  denied"  error  for  a  script?

●  Answer:

Check  file  permissions:

ls  -l  script.sh   Add  execute  permission:

chmod  +x  script.sh

Q19:  How  do  you  extend  a  mounted  LVM  partition?

●  Answer:

Increase  the  logical  volume:

sudo  lvextend  -L  +10G  /dev/mapper/vol_group-lv_name

## Page 8

Resize  the  filesystem:  sudo  resize2fs  /dev/mapper/vol_group-lv_name

Q20:  How  do  you  find  the  top  10  largest  files  in  a  directory?

Answer:

find  /path/to/dir  -type  f  -exec  du  -h  {}  +  |  sort  -rh  |  head

- n
10

Backup  and  Restore

Q21:  How  do  you  back  up  a  directory  using  rsync?

Answer:  rsync  -av  /source/directory  /destination/directory

○  -a:  Archive  mode.  ○  -v:  Verbose  output.

Q22:  How  do  you  restore  files  from  a  tar  backup?

Answer:  tar  -xvf  backup.tar  -C  /restore/path

Q23:  How  do  you  rotate  logs  manually?

●  Answer:

Use  logrotate:

sudo  logrotate  /etc/logrotate.conf  --force

Q24:  How  do  you  view  the  last  50  lines  of  a  log  file?

## Page 9

Answer:  tail  -n  50  /var/log/syslog

Q25:  How  do  you  check  which  kernel  modules  are  currently  loaded?

Answer:  lsmod

Q26:  How  do  you  load  a  kernel  module  manually?

Answer:  sudo  modprobe  <module_name>

Q27:  How  do  you  lock  a  user  account?

Answer:  sudo  passwd  -l  username

Q28:  How  do  you  check  the  groups  a  user  belongs  to?

Answer:  groups  username

Q29:  How  do  you  check  the  installed  Linux  distribution?

Answer:  lsb_release  -a   Or:

cat  /etc/os-release

Q30:  How  do  you  list  installed  packages  in  RHEL/CentOS?

## Page 10

Answer:  yum  list  installed

Q31:  How  do  you  list  all  running  virtual  machines  in  KVM?

Answer:  virsh  list

Q32:  How  do  you  create  a  virtual  machine  in  VirtualBox  from  the  command  line?

Answer:  VBoxManage  createvm  --name  VMName  --register

Q33:  How  do  you  check  running  Docker  containers?

Answer:  docker  ps

Q34:  How  do  you  restart  a  Kubernetes  pod?

Answer:  kubectl  rollout  restart  deployment  <deployment_name>

Q35:  How  do  you  troubleshoot  if  a  Linux  system  fails  to  boot?

●  Answer:  1.  Boot  into  recovery  mode  or  single-user  mode.  2.  Check  logs  in  /var/log/boot.log or  /var/log/messages.

Verify  the  GRUB  configuration:  cat  /boot/grub2/grub.cfg   Check  disk  integrity:

## Page 11

fsck  /dev/sdX   Reinstall  GRUB  if  required:

grub2-install  /dev/sdX

Q36:  What  is  the  role  of  the  init system  in  Linux?

●  Answer:  ○  The  init system  is  the  first  process  started  by  the  kernel  after  booting.  ○  It  initializes  the  system  by  starting  necessary  services  and  managing

runlevels

(or

targets

in

systemd).

Q37:  How  do  you  check  the  open  ports  on  a  Linux  server?

Answer:  sudo  netstat  -tuln   Or  using  ss:

ss  -tuln

Q38:  How  do  you  add  a  persistent  static  route  in  Linux?

●  Answer:  ○  Edit  the  network  configuration  file:

RHEL/CentOS:  vi  /etc/sysconfig/network-scripts/route-eth0  Add:  192.168.2.0/24  via  192.168.1.1  dev  eth0 Restart  the  network  service:  sudo  systemctl  restart  network

## Page 12

Q39:  How  do  you  list  all  installed  packages  on  an  Ubuntu  system?

Answer:  dpkg  --get-selections

Q40:  How  do  you  remove  a  package  along  with  its  configuration  files  in

Debian/Ubuntu?

Answer:  sudo  apt-get  purge  <package_name>

Q41:  How  do  you  check  for  disk  usage  by  each  directory  in  the  current  path?

Answer:  du  -sh  *

Q42:  How  do  you  create  and  mount  an  ext4  filesystem?

●  Answer:

Create  the  filesystem:

mkfs.ext4  /dev/sdX   Mount  the  filesystem:

mount  /dev/sdX  /mnt

Q43:  How  do  you  find  out  which  process  is  using  the  most  memory?

Answer:  ps  aux  --sort=-%mem  |  head

Q44:  How  do  you  monitor  live  network  traffic  on  an  interface?

Answer:

## Page 13

sudo  tcpdump  -i  eth0

Q45:  How  do  you  change  the  priority  of  a  running  process?

●  Answer:

Use  the  renice command:  sudo  renice  -n  10  -p  <PID>

○  10:  New  priority  value.

Q46:  How  do  you  restart  a  failed  systemd  service?

Answer:  sudo  systemctl  restart  <service_name>

Q47:  How  do  you  generate  an  SSH  key  pair?

Answer:  ssh-keygen  -t  rsa  -b  4096  -C  "your_email@example.com"

○  -t  rsa:  Specifies  the  key  type.  ○  -b  4096:  Sets  the  key  length.

Q48:  How  do  you  prevent  a  user  from  logging  in  via  SSH?

●  Answer:

Add  the  user  to  /etc/ssh/sshd_config:  DenyUsers  username   Restart  the  SSH  service:  sudo  systemctl  restart  sshd

## Page 14

Q49:  How  do  you  find  specific  error  messages  in  a  log  file?

Answer:  grep  "ERROR"  /var/log/syslog

Q50:  How  do  you  monitor  a  log  file  in  real-time?

Answer:  tail  -f  /var/log/syslog

Q51:  How  do  you  check  the  current  Linux  kernel  version?

Answer:  uname  -r

Q52:  How  do  you  remove  a  kernel  module?

Answer:  sudo  rmmod  <module_name>

Q53:  How  do  you  create  a  group  and  add  a  user  to  it?

●  Answer:

Create  the  group:  sudo  groupadd  groupname   Add  the  user:  sudo  usermod  -aG  groupname  username

Q54:  How  do  you  delete  a  user  and  their  home  directory?

Answer:  sudo  userdel  -r  username

## Page 15

Q55:  Write  a  script  to  print  the  number  of  files  in  a  directory.

Answer:  #!/bin/  DIR=$1  if  [  -d  "$DIR"  ];  then      echo  "Number  of  files  in  $DIR:  $(ls  -1  $DIR  |  wc  -l)"  else      echo  "$DIR  is  not  a  directory."  fi

Q56:  How  do  you  test  if  a  specific  port  on  a  remote  server  is  open?

Answer:  nc  -zv  <server_ip>  <port>

○  -z:  Scans  without  sending  data.  ○  -v:  Enables  verbose  output.

Q57:  How  do  you  flush  the  DNS  cache  in  Linux?

●  Answer:

For  systemd-resolved:  sudo  systemd-resolve  --flush-caches   Verify:  sudo  systemd-resolve  --statistics

Q58:  How  do  you  check  which  services  are  enabled  to  start  at  boot?

Answer:  systemctl  list-unit-files  --type=service  |  grep  enabled

## Page 16

Q59:  How  do  you  stop  a  service  and  ensure  it  doesn’t  start  at  boot?

Answer:  sudo  systemctl  stop  <service_name>  sudo  systemctl  disable  <service_name>

Q60:  How  do  you  check  memory  usage  in  Linux?

Answer:  free  -m

○  Or  using  top or  htop for  a  real-time  view.

Q61:  How  do  you  identify  zombie  processes?

Answer:  ps  aux  |  grep  'Z'

○  A  zombie  process  will  have  a  status  of  Z.

Q62:  Write  a  script  to  monitor  disk  usage  and  send  an  email  alert  if  usage  exceeds

80%.

Answer:  #!/bin/  THRESHOLD=80  USAGE=$(df  -h  /  |  grep  -v  Filesystem  |  awk  '{print  $5}'  |

sed

's/%//')

if  [  "$USAGE"  -gt  "$THRESHOLD"  ];  then      echo  "Disk  usage  is  at  ${USAGE}%  on  $(hostname)"  |  mail

- s
"Disk

Usage

Alert"

user@example.com

fi

Q63:  Write  a  script  to  check  if  a  service  is  running  and  restart  it  if  it’s  not.

## Page 17

Answer:  #!/bin/  SERVICE=nginx  if  !  systemctl  is-active  --quiet  $SERVICE;  then      systemctl  restart  $SERVICE      echo  "$SERVICE  was  down  and  has  been  restarted."  else      echo  "$SERVICE  is  running."  fi

Q64:  How  do  you  unmount  a  busy  filesystem?

●  Answer:

Identify  processes  using  the  filesystem:

lsof  |  grep  /path/to/mount   Kill  those  processes:

kill  -9  <PID>   Unmount  the  filesystem:

sudo  umount  /path/to/mount

Q65:  How  do  you  create  a  swap  file?

●  Answer:

Create  the  file:  sudo  dd  if=/dev/zero  of=/swapfile  bs=1G  count=2

## Page 18

Set  permissions:

sudo  chmod  600  /swapfile   Set  up  the  swap  space:

sudo  mkswap  /swapfile  sudo  swapon  /swapfile   Make  it  persistent:

echo  '/swapfile  none  swap  sw  0  0'  |  sudo  tee  -a  /etc/fstab

Q66:  How  do  you  check  for  failed  login  attempts?

Answer:  sudo  grep  "Failed  password"  /var/log/auth.log

Q67:  How  do  you  restrict  a  user  to  their  home  directory  using  SSH?

●  Answer:

Edit  /etc/ssh/sshd_config:

Match  User  username      ChrootDirectory  /home/username      AllowTCPForwarding  no      X11Forwarding  no   Restart  the  SSH  service:  sudo  systemctl  restart  sshd

## Page 19

Q68:  How  do  you  take  a  snapshot  of  an  LVM  volume?

●  Answer:

Create  a  snapshot:  sudo  lvcreate  --size  1G  --snapshot  --name  snap_name

/dev/vol_group/lv_name

Mount  the  snapshot  (optional):

sudo  mount  /dev/vol_group/snap_name  /mnt

Q69:  How  do  you  schedule  a  daily  backup  with  cron?

●  Answer:

Edit  the  cron  jobs:

crontab  -e   Add  the  job:

0  2  *  *  *  tar  -czf  /backup/$(date  +\%F).tar.gz  /data

Q70:  How  do  you  compress  log  files  older  than  30  days?

Answer:  find  /var/log  -type  f  -mtime  +30  -exec  gzip  {}  \;

Q71:  How  do  you  rotate  logs  for  a  custom  application?

●  Answer:

## Page 20

Create  a  logrotate  configuration  file:  sudo  vi  /etc/logrotate.d/custom_app   Add  the  configuration:  /var/log/custom_app/*.log  {      daily      rotate  7      compress      missingok      notifempty  } Test  the  configuration:  sudo  logrotate  -d  /etc/logrotate.d/custom_app

Q72:  How  do  you  list  all  available  kernel  versions?

Answer:

dpkg  --list  |  grep  linux-image

Q73:  How  do  you  update  the  Linux  kernel?

●  Answer:

For  Debian/Ubuntu:

sudo  apt-get  update  sudo  apt-get  upgrade  linux-image-$(uname  -r)

Q74:  How  do  you  update  all  installed  packages  on  a  CentOS  system?

## Page 21

Answer:  sudo  yum  update

Q75:  How  do  you  check  dependencies  for  a  package  in  Ubuntu?

Answer:  apt-cache  depends  <package_name>

Q76:  How  do  you  configure  a  static  IP  address  on  a  Linux  server?

●  Answer:  ○  For  RHEL/CentOS:

Edit  the  network  configuration  file:  sudo  vi  /etc/sysconfig/network-scripts/ifcfg-eth0   Add  or  update:

makefile

BOOTPROTO=static  IPADDR=192.168.1.100  NETMASK=255.255.255.0  GATEWAY=192.168.1.1  DNS1=8.8.8.8   Restart  the  network:

sudo  systemctl  restart  network

Q77:  How  do  you  check  the  default  gateway  on  a  Linux  system?

Answer:

## Page 22

ip  route  |  grep  default

Q78:  How  do  you  find  the  parent  process  of  a  given  process?

Answer:  ps  -o  ppid=  -p  <PID>

Q79:  How  do  you  kill  all  processes  owned  by  a  specific  user?

Answer:  sudo  pkill  -u  <username>

Q80:  How  do  you  generate  a  CPU  usage  report  over  time?

Answer:  sar  -u  1  10

○  -u:  CPU  usage.  ○  1  10:  Sample  every  1  second  for  10  intervals.

Q81:  How  do  you  monitor  real-time  I/O  usage  per  process?

Answer:  iotop

Q82:  Write  a  script  to  display  the  top  5  largest  files  in  a  directory.

Answer:

#!/bin/  du  -ah  $1  |  sort  -rh  |  head  -n  5

Q83:  Write  a  script  to  automate  user  creation  and  password  assignment.

## Page 23

Answer:  #!/bin/  USER=$1  PASS=$2  sudo  useradd  -m  $USER  echo  "$USER:$PASS"  |  sudo  chpasswd  echo  "User  $USER  created  with  the  given  password."

Q84:  How  do  you  repair  a  corrupted  filesystem?

●  Answer:

Unmount  the  filesystem:  sudo  umount  /dev/sdX   Run  fsck:

sudo  fsck  -y  /dev/sdX

Q85:  How  do  you  check  the  inode  usage  on  a  filesystem?

Answer:  df  -i

Q86:  How  do  you  disable  root  login  over  SSH?

●  Answer:

Edit  the  SSH  configuration  file:  sudo  vi  /etc/ssh/sshd_config   Update  or  add:

## Page 24

perl

PermitRootLogin  no   Restart  the  SSH  service:

sudo  systemctl  restart  sshd

Q87:  How  do  you  configure  a  Linux  firewall  to  allow  only  HTTP  and  SSH  traffic?

Answer:  sudo  ufw  allow  ssh  sudo  ufw  allow  http  sudo  ufw  enable

Q88:  How  do  you  schedule  a  weekly  backup  of  the  /home directory?

●  Answer:

Create  a  backup  script:

vi  /usr/local/bin/backup.sh  Add:

#!/bin/  tar  -czf  /backup/home_$(date  +%F).tar.gz  /home   Make  the  script  executable:

chmod  +x  /usr/local/bin/backup.sh   Add  to  cron:

## Page 25

crontab  -e  Add:

0  3  *  *  0  /usr/local/bin/backup.sh

Q89:  How  do  you  restore  files  from  a  compressed  tar  archive?

Answer:

tar  -xvzf  backup.tar.gz  -C  /restore/path

Q90:  How  do  you  clear  logs  without  deleting  the  file?

Answer:

sudo  truncate  -s  0  /var/log/syslog

Q91:  How  do  you  archive  logs  older  than  60  days?

Answer:

find  /var/log  -type  f  -mtime  +60  -exec  tar  -rvf  old_logs.tar

{}

\;

- exec
rm

{}

\;

Q92:  How  do  you  rebuild  the  initramfs  image?

Answer:

sudo  dracut  -f

Q93:  How  do  you  blacklist  a  kernel  module?

●  Answer:

Add  the  module  name  to  /etc/modprobe.d/blacklist.conf:

## Page 26

echo  "blacklist  <module_name>"  |  sudo  tee  -a

/etc/modprobe.d/blacklist.conf

Regenerate  the  initramfs:

sudo  dracut  -f

Q94:  How  do  you  check  which  package  owns  a  specific  file?

●  Answer:

For  Debian/Ubuntu:

dpkg  -S  /path/to/file   For  RHEL/CentOS:

rpm  -qf  /path/to/file

Q95:  How  do  you  clean  up  cached  package  files  in  CentOS?

Answer:

sudo  yum  clean  all

Q96:  How  do  you  list  available  virtual  machines  in  KVM?

Answer:

virsh  list  --all

Q97:  How  do  you  take  a  snapshot  of  a  running  VM  in  KVM?

Answer:

## Page 27

virsh  snapshot-create-as  <vm_name>  <snapshot_name>

Q98:  How  do  you  restart  all  Docker  containers?

Answer:

docker  restart  $(docker  ps  -q)

Q99:  How  do  you  check  the  status  of  Kubernetes  pods?

Answer:

kubectl  get  pods

Q100:  How  do  you  determine  the  Linux  distribution  and  version?

Answer:

lsb_release  -a   Or:

cat  /etc/os-release

Q101:  How  do  you  test  network  connectivity  using  ping and  set  a  timeout?

Answer:

ping  -c  4  -W  2  <host>

○  -c  4:  Sends  4  packets.  ○  -W  2:  Sets  a  timeout  of  2  seconds.

Q102:  How  do  you  check  active  network  connections  on  a  system?

## Page 28

Answer:

netstat  -an   Or:

ss  -tunap

Q103:  How  do  you  schedule  a  process  to  run  at  a  specific  time  using  at?

●  Answer:

Install  at if  not  already  available:

sudo  apt  install  at   Use  the  at command:

echo  "service  apache2  restart"  |  at  02:00

Q104:  How  do  you  view  the  priority  of  a  running  process?

Answer:

ps  -eo  pid,ni,comm  |  grep  <process_name>

○  ni:  Displays  the  process's  nice  value.

Q105:  How  do  you  monitor  memory  usage  for  a  specific  process?

Answer:

pmap  <PID>  |  grep  total

## Page 29

○  pmap:  Displays  memory  map  of  a  process.

Q106:  How  do  you  find  the  top  5  CPU-consuming  processes?

Answer:  ps  -eo  pid,ppid,cmd,%mem,%cpu  --sort=-%cpu  |  head  -n  5

Q107:  Write  a  script  to  check  if  a  directory  exists  and  create  it  if  not.

Answer:

#!/bin/  DIR=$1  if  [  !  -d  "$DIR"  ];  then      mkdir  -p  "$DIR"      echo  "Directory  $DIR  created."  else      echo  "Directory  $DIR  already  exists."  fi

Q108:  Write  a  script  to  calculate  the  factorial  of  a  given  number.

Answer:

#!/bin/  factorial=1  for  ((  i=1;  i<=$1;  i++  ))  do      factorial=$((factorial  *  i))  done  echo  "Factorial  of  $1  is  $factorial"

## Page 30

Q109:  How  do  you  display  disk  usage  for  a  specific  directory  in  a  human-readable

format?

Answer:

du  -sh  /path/to/directory

Q110:  How  do  you  check  for  filesystem  errors  on  a  specific  partition?

Answer:

sudo  fsck  /dev/sdX

Q111:  How  do  you  enforce  password  expiration  for  a  user?

Answer:

sudo  chage  -M  30  username

○  -M  30:  Sets  the  maximum  number  of  days  before  password  expiration.

Q112:  How  do  you  set  up  a  firewall  rule  to  block  all  incoming  traffic  except  SSH?

Answer:

sudo  ufw  default  deny  incoming  sudo  ufw  allow  ssh  sudo  ufw  enable

Q113:  How  do  you  compress  and  back  up  a  MySQL  database?

Answer:

## Page 31

mysqldump  -u  root  -p  database_name  |  gzip  >

database_backup.sql.gz

Q114:  How  do  you  restore  a  database  from  a  compressed  backup?

Answer:

gunzip  <  database_backup.sql.gz  |  mysql  -u  root  -p

database_name

Q115:  How  do  you  view  only  the  last  10  lines  of  multiple  log  files?

Answer:

tail  -n  10  /var/log/*.log

Q116:  How  do  you  delete  log  files  older  than  90  days?

Answer:

find  /var/log  -type  f  -mtime  +90  -exec  rm  -f  {}  \;

Q117:  How  do  you  enable  or  disable  a  kernel  module  at  runtime?

●  Answer:

Enable:

sudo  modprobe  <module_name>   Disable:

sudo  rmmod  <module_name>

Q118:  How  do  you  check  the  kernel  boot  parameters?

## Page 32

Answer:

cat  /proc/cmdline

Q119:  How  do  you  list  all  available  updates  for  an  Ubuntu  system?

Answer:

sudo  apt  list  --upgradable

Q120:  How  do  you  install  a  package  from  a  .rpm file  in  CentOS?

Answer:

sudo  rpm  -ivh  package.rpm

Q121:  How  do  you  shut  down  a  running  VM  in  KVM?

Answer:

virsh  shutdown  <vm_name>

Q122:  How  do  you  configure  a  network  bridge  for  a  VM  in  KVM?

●  Answer:

Edit  the  network  configuration  file:

sudo  vi  /etc/sysconfig/network-scripts/ifcfg-br0 Add  bridge  configuration:

makefile

## Page 33

DEVICE=br0  TYPE=Bridge  BOOTPROTO=dhcp  ONBOOT=yes

Q123:  How  do  you  check  the  logs  of  a  specific  Docker  container?

Answer:

docker  logs  <container_id>

Q124:  How  do  you  delete  all  stopped  Docker  containers?

Answer:

docker  container  prune

Q125:  How  do  you  display  the  currently  logged-in  users?

Answer:

who

Q126:  How  do  you  set  an  environment  variable  permanently  for  a  user?

●  Answer:

Add  the  variable  to  the  user’s  .rc file:

echo  "export  VAR_NAME=value"  >>  ~/.rc   Reload  the  shell:

source  ~/.rc

## Page 34

Q127:  How  do  you  troubleshoot  if  a  specific  port  is  not  accessible  on  a  server?

●  Answer:

Check  if  the  service  is  running:

sudo  systemctl  status  <service_name>   Verify  if  the  port  is  open:

sudo  netstat  -tuln  |  grep  <port>   Check  firewall  rules:

sudo  ufw  status   Test  connectivity  using  telnet or  nc:

telnet  <server_ip>  <port>

1.  Inspect  logs  for  errors  in  /var/log.
Q128:  How  do  you  configure  DNS  resolution  in  Linux?

●  Answer:

Edit  the  /etc/resolv.conf file:

nameserver  8.8.8.8  nameserver  8.8.4.4   Save  and  test  using:

## Page 35

nslookup  google.com

Q129:  How  do  you  restart  a  service  automatically  if  it  crashes?

●  Answer:

Create  a  systemd  service  file  or  edit  an  existing  one:

sudo  vi  /etc/systemd/system/<service_name>.service   Add  the  following  lines  under  [Service]:

makefile

Restart=always  RestartSec=5   Reload  systemd  and  enable  the  service:

sudo  systemctl  daemon-reload  sudo  systemctl  enable  <service_name>

Q130:  How  do  you  check  all  processes  owned  by  a  specific  user?

Answer:

ps  -u  <username>

Q131:  How  do  you  monitor  network  bandwidth  usage  in  real-time?

Answer:

iftop  -i  <interface>

## Page 36

Or:

nload  <interface>

Q132:  How  do  you  generate  a  CPU  usage  report  for  the  past  hour?

Answer:

sar  -u  -s  HH:MM  -e  HH:MM

○  Replace  HH:MM with  the  time  range.

Q133:  Write  a  script  to  check  if  a  website  is  reachable.

Answer:

#!/bin/  WEBSITE=$1  if  curl  -Is  $WEBSITE  |  grep  "200  OK";  then      echo  "$WEBSITE  is  reachable."  else      echo  "$WEBSITE  is  not  reachable."  fi

Q134:  Write  a  script  to  back  up  a  directory  and  log  the  output.

Answer:

#!/bin/  DIR=$1  BACKUP_DIR="/backup/$(date  +%F)"

## Page 37

mkdir  -p  $BACKUP_DIR  tar  -czf  $BACKUP_DIR/backup.tar.gz  $DIR  >

/var/log/backup.log

2>&1

echo  "Backup  completed.  Log  available  at

/var/log/backup.log."

Q135:  How  do  you  add  a  new  disk  to  an  existing  Linux  system  without  rebooting?

●  Answer:

Scan  for  new  disks:

sudo  partprobe   Create  a  partition:

sudo  fdisk  /dev/sdX   Create  a  filesystem:

sudo  mkfs.ext4  /dev/sdX1   Mount  the  partition:

sudo  mount  /dev/sdX1  /mnt

Q136:  How  do  you  increase  the  size  of  an  existing  filesystem?

●  Answer:

Extend  the  logical  volume:  sudo  lvextend  -L  +10G  /dev/vol_group/lv_name

## Page 38

Resize  the  filesystem:

sudo  resize2fs  /dev/vol_group/lv_name

Q137:  How  do  you  enable  auditing  on  a  file?

●  Answer:

Install  auditd if  not  already  available:

sudo  apt  install  auditd   Add  a  rule:

sudo  auditctl  -w  /path/to/file  -p  rwxa  -k  file_audit   Check  logs:

sudo  ausearch  -k  file_audit

Q138:  How  do  you  disable  password-based  SSH  authentication?

●  Answer:

Edit  /etc/ssh/sshd_config:

PasswordAuthentication  no   Restart  the  SSH  service:

sudo  systemctl  restart  sshd

## Page 39

Q139:  How  do  you  take  an  incremental  backup  with  rsync?

Answer:

rsync  -av  --delete  /source  /destination

Q140:  How  do  you  restore  a  specific  file  from  a  tar  archive?

Answer:

tar  -xvzf  backup.tar.gz  path/to/file

Q141:  How  do  you  find  the  most  frequent  error  in  a  log  file?

Answer:

grep  "ERROR"  /var/log/syslog  |  awk  '{print  $NF}'  |  sort  |

uniq

- c
|

sort

- nr
|

head

- n
1

Q142:  How  do  you  configure  centralized  log  management  using  rsyslog?

●  Answer:

On  the  client,  edit  /etc/rsyslog.conf:

- .*  @logserver_ip:514   Restart  the  rsyslog service:
sudo  systemctl  restart  rsyslog

Q143:  How  do  you  verify  kernel  parameters  in  Linux?

Answer:

## Page 40

sysctl  -a

Q144:  How  do  you  temporarily  modify  a  kernel  parameter?

Answer:

sudo  sysctl  -w  net.ipv4.ip_forward=1

Q145:  How  do  you  search  for  a  package  using  yum?

Answer:

sudo  yum  search  <package_name>

Q146:  How  do  you  install  a  package  from  a  .deb file?

Answer:

sudo  dpkg  -i  package.deb  sudo  apt-get  install  -f

Q147:  How  do  you  clone  a  virtual  machine  in  KVM?

Answer:

virt-clone  --original  <vm_name>  --name  <new_vm_name>  --file

/var/lib/libvirt/images/new_vm.img

Q148:  How  do  you  check  the  virtualized  environment  of  a  Linux  system?

Answer:

sudo  dmidecode  -s  system-product-name

## Page 41

Q149:  How  do  you  delete  unused  Docker  images?

Answer:

docker  image  prune

Q150:  How  do  you  deploy  a  Kubernetes  pod  using  a  YAML  file?

Answer:

kubectl  apply  -f  pod.yaml

Q151:  How  do  you  find  the  IP  address  of  your  Linux  machine?

Answer:

ip  addr  show   Or  for  a  specific  interface:

ip  addr  show  eth0

Q152:  How  do  you  capture  network  packets  on  a  specific  interface?

Answer:

sudo  tcpdump  -i  eth0

Q153:  How  do  you  list  all  active  and  inactive  services?

Answer:

systemctl  list-units  --type=service

## Page 42

Q154:  How  do  you  view  the  startup  services  and  their  statuses?

Answer:

sudo  systemctl  list-unit-files  --type=service

Q155:  How  do  you  analyze  disk  I/O  performance?

Answer:

iostat  -d  -x  2

○  -d:  Displays  device  utilization.  ○  -x:  Displays  extended  statistics.

Q156:  How  do  you  display  a  summary  of  system  performance?

Answer:

vmstat  1  5

○  1  5:  Collects  data  every  second  for  5  iterations.

Q157:  Write  a  script  to  count  the  number  of  users  currently  logged  in.

Answer:

#!/bin/  echo  "Number  of  logged-in  users:  $(who  |  wc  -l)"

Q158:  Write  a  script  to  check  disk  usage  and  send  an  email  alert  if  it  exceeds  90%.

Answer:

## Page 43

#!/bin/  THRESHOLD=90  USAGE=$(df  -h  /  |  grep  /  |  awk  '{print  $5}'  |  sed  's/%//')  if  [  "$USAGE"  -gt  "$THRESHOLD"  ];  then      echo  "Disk  usage  is  at  ${USAGE}%  on  $(hostname)"  |  mail

- s
"Disk

Usage

Alert"

admin@example.com

fi

Q159:  How  do  you  remove  a  mount  point  that  is  in  use?

●  Answer:

Identify  processes  using  the  mount  point:

lsof  |  grep  /mount/point   Kill  the  processes:

kill  -9  <PID>   Unmount:

sudo  umount  /mount/point

Q160:  How  do  you  find  disk  partitions  and  their  usage?

Answer:

lsblk

Q161:  How  do  you  add  a  user  to  the  sudo group?

Answer:

## Page 44

sudo  usermod  -aG  sudo  username

Q162:  How  do  you  check  for  open  ports  on  your  system?

Answer:

sudo  netstat  -tuln   Or:

sudo  ss  -tuln

Q163:  How  do  you  set  up  an  automatic  daily  backup  using  cron?

●  Answer:

Create  a  script:

vi  /usr/local/bin/daily_backup.sh

Add:

#!/bin/  tar  -czf  /backup/$(date  +%F).tar.gz  /data   Make  it  executable:

chmod  +x  /usr/local/bin/daily_backup.sh   Add  to  cron:

crontab  -e  Add:

## Page 45

0  3  *  *  *  /usr/local/bin/daily_backup.sh

Q164:  How  do  you  restore  files  from  an  incremental  backup?

●  Answer:

Extract  the  full  backup  first:

tar  -xvzf  full_backup.tar.gz  -C  /restore_path   Extract  the  incremental  backups  in  order:

tar  -xvzf  incremental_backup.tar.gz  -C  /restore_path

Q165:  How  do  you  monitor  log  files  in  real-time  for  multiple  files?

Answer:

multitail  /var/log/file1  /var/log/file2

Q166:  How  do  you  rotate  logs  for  a  specific  application?

●  Answer:

Create  a  logrotate  config:

sudo  vi  /etc/logrotate.d/app_name   Add:

/var/log/app_name/*.log  {      daily      rotate  5

## Page 46

compress      missingok      notifempty  }   Test:

sudo  logrotate  -d  /etc/logrotate.d/app_name

Q167:  How  do  you  enable  IP  forwarding  temporarily?

Answer:

sudo  sysctl  -w  net.ipv4.ip_forward=1

Q168:  How  do  you  list  loaded  kernel  modules  with  descriptions?

Answer:

lsmod  |  column  -t

Q169:  How  do  you  remove  a  package  and  its  dependencies  in  Ubuntu?

Answer:

sudo  apt-get  autoremove  --purge  <package_name>

Q170:  How  do  you  upgrade  a  specific  package  in  CentOS?

Answer:

sudo  yum  update  <package_name>

## Page 47

Q171:  How  do  you  create  a  snapshot  of  a  virtual  machine  in  KVM?

Answer:

virsh  snapshot-create-as  <vm_name>  <snapshot_name>

Q172:  How  do  you  configure  networking  for  a  VM  to  use  NAT  in  KVM?

●  Answer:

Edit  the  virsh network  configuration:

virsh  net-edit  default

1.  Ensure  the  <forward  mode='nat'/> tag  is  present.
Q173:  How  do  you  restart  a  Kubernetes  deployment?

Answer:

kubectl  rollout  restart  deployment  <deployment_name>

Q174:  How  do  you  inspect  the  Docker  network?

Answer:

docker  network  inspect  <network_name>

Q175:  How  do  you  set  a  default  editor  for  the  terminal?

Answer:

## Page 48

export  EDITOR=vim   To  make  it  persistent:

echo  "export  EDITOR=vim"  >>  ~/.rc  source  ~/.rc

Q176:  How  do  you  schedule  a  one-time  job  using  at?

Answer:

echo  "shutdown  -h  now"  |  at  23:00

Q177:  How  do  you  add  a  static  route  in  Linux?

●  Answer:

Add  a  temporary  route:

sudo  ip  route  add  192.168.2.0/24  via  192.168.1.1  dev  eth0

1.  Add  a  persistent  route:
For  RHEL/CentOS,  edit  /etc/sysconfig/network-scripts/route-eth0 and

add:

192.168.2.0/24  via  192.168.1.1
Q178:  How  do  you  troubleshoot  high  network  latency?

●  Answer:

Check  connectivity  with  ping:

## Page 49

ping  <destination>   Trace  the  network  path  with  traceroute:

traceroute  <destination>   Inspect  network  traffic:

sudo  tcpdump  -i  eth0   Monitor  interface  statistics:

ifconfig  eth0

Q179:  How  do  you  set  CPU  affinity  for  a  process?

Answer:

taskset  -c  0,1  <PID>

○  This  assigns  the  process  to  CPUs  0  and  1.

Q180:  How  do  you  view  the  system  logs  of  a  specific  service?

Answer:

journalctl  -u  <service_name>

Q181:  How  do  you  check  the  uptime  of  a  system?

Answer:

Uptime

## Page 50

Q182:  How  do  you  monitor  disk  throughput  in  real-time?

Answer:

iotop

Q183:  Write  a  script  to  monitor  a  directory  and  log  changes.

Answer:

#!/bin/  inotifywait  -m  /path/to/directory  -e  create  -e  delete  -e

modify

|

while  read  path  action  file;  do      echo  "[$(date)]  $file  was  $action  in  $path"  >>

/var/log/dir_changes.log

done

Q184:  Write  a  script  to  send  an  email  alert  if  a  service  is  down.

Answer:

#!/bin/  SERVICE=nginx  if  !  systemctl  is-active  --quiet  $SERVICE;  then      echo  "$SERVICE  is  down  on  $(hostname)"  |  mail  -s

"Service

Alert"

admin@example.com

fi

Q185:  How  do  you  mount  a  filesystem  at  boot?

●  Answer:

## Page 51

Add  an  entry  in  /etc/fstab:

/dev/sdX1   /mnt/data   ext4   defaults   0   2   Test  the  entry:

sudo  mount  -a

Q186:  How  do  you  increase  the  size  of  a  swap  file?

●  Answer:

Turn  off  the  current  swap  file:

sudo  swapoff  /swapfile   Resize  the  swap  file:

sudo  dd  if=/dev/zero  of=/swapfile  bs=1G  count=4   Set  it  up  again:

sudo  mkswap  /swapfile  sudo  swapon  /swapfile

Q187:  How  do  you  configure  SSH  key-based  authentication?

●  Answer:

Generate  a  key  pair:  ssh-keygen  -t  rsa

## Page 52

Copy  the  public  key  to  the  remote  server:

ssh-copy-id  user@remote_server   Verify  login:

ssh  user@remote_server

Q188:  How  do  you  block  an  IP  address  using  iptables?

Answer:

sudo  iptables  -A  INPUT  -s  <IP_ADDRESS>  -j  DROP

Q189:  How  do  you  create  a  snapshot  of  an  LVM  volume?

●  Answer:

Create  the  snapshot:

sudo  lvcreate  --size  1G  --snapshot  --name  snap_name

/dev/vol_group/lv_name

Mount  the  snapshot:

sudo  mount  /dev/vol_group/snap_name  /mnt

Q190:  How  do  you  restore  a  system  from  a  tar  backup?

Answer:

tar  -xvzf  backup.tar.gz  -C  /

## Page 53

Q191:  How  do  you  configure  remote  logging  using  rsyslog?

●  Answer:

On  the  client  machine,  edit  /etc/rsyslog.conf:

- .*  @<log_server_ip>:514   Restart  the  rsyslog service:
sudo  systemctl  restart  rsyslog

Q192:  How  do  you  analyze  logs  for  the  most  common  HTTP  errors?

Answer:

cat  /var/log/httpd/access.log  |  awk  '{print  $9}'  |  sort  |

uniq

- c
|

sort

- nr
Q193:  How  do  you  persist  kernel  parameter  changes?

●  Answer:

Add  the  parameter  to  /etc/sysctl.conf:

net.ipv4.ip_forward=1   Apply  the  changes:  sudo  sysctl  -p

Q194:  How  do  you  display  CPU  information?

## Page 54

Answer:  cat  /proc/cpuinfo

Q195:  How  do  you  verify  the  integrity  of  a  package  in  CentOS?

Answer:

rpm  -V  <package_name>

Q196:  How  do  you  list  dependencies  for  a  package  in  Ubuntu?

Answer:

apt-cache  depends  <package_name>

Q197:  How  do  you  migrate  a  VM  to  another  host  in  KVM?

Answer:

virsh  migrate  --live  <vm_name>

qemu+ssh://<destination_host>/system

Q198:  How  do  you  resize  a  virtual  disk  in  KVM?

●  Answer:

Resize  the  disk:

qemu-img  resize  /path/to/disk.img  +10G

1.  Extend  the  filesystem  inside  the  VM.
## Page 55

Q199:  How  do  you  update  an  image  in  a  Kubernetes  deployment?

Answer:

kubectl  set  image  deployment/<deployment_name>

<container_name>=<new_image>

Q200:  How  do  you  clean  up  unused  volumes  in  Docker?

Answer:

docker  volume  prune

Q201:  How  do  you  configure  a  bonded  network  interface  in  Linux?

●  Answer:

Install  the  bonding  module:

sudo  modprobe  bonding

1.  Configure  the  bond  in  /etc/network/interfaces (Debian/Ubuntu)
- r
/etc/sysconfig/network-scripts/ifcfg-bond0

(RHEL/CentOS).

Q202:  How  do  you  troubleshoot  DNS  resolution  issues?

●  Answer:  1.  Check  /etc/resolv.conf for  DNS  server  entries.

Test  resolution:

nslookup  google.com

## Page 56

Use  dig for  detailed  DNS  queries:

dig  google.com

Q203:  How  do  you  debug  a  hung  process  in  Linux?

●  Answer:

Check  the  state  of  the  process:

ps  -o  stat=  -p  <PID>   Use  strace to  trace  system  calls:

strace  -p  <PID>

Q204:  How  do  you  enable  a  service  to  start  on  boot?

Answer:

sudo  systemctl  enable  <service_name>

Q205:  How  do  you  analyze  system  load  averages?

Answer:  Use  the  uptime or  top command:

uptime

○  Load  averages  represent  the  number  of  processes  waiting  for  CPU  over  1,

5,

and

15

minutes.

Q206:  How  do  you  find  disk  latency  using  iostat?

## Page 57

Answer:

iostat  -x

○  Check  await and  svctm columns  for  latency.

Q207:  Write  a  script  to  find  the  largest  file  in  a  directory.

Answer:

#!/bin/  find  $1  -type  f  -exec  du  -h  {}  +  |  sort  -rh  |  head  -n  1

Q208:  Write  a  script  to  list  all  installed  packages  and  save  them  to  a  file.

Answer:

#!/bin/  dpkg  --get-selections  >  installed_packages.txt

Q209:  How  do  you  check  the  health  of  a  hard  drive?

Answer:

sudo  smartctl  -H  /dev/sdX

Q210:  How  do  you  enable  quotas  on  a  filesystem?

●  Answer:

Mount  the  filesystem  with  quota  options:

sudo  mount  -o  remount,usrquota,grpquota  /dev/sdX  /mnt

## Page 58

Create  quota  files:

sudo  touch  /mnt/aquota.user  /mnt/aquota.group  sudo  chmod  600  /mnt/aquota.*  sudo  quotacheck  -cug  /mnt   Enable  quotas:

sudo  quotaon  /mnt

Q211:  How  do  you  monitor  failed  login  attempts?

Answer:

sudo  grep  "Failed  password"  /var/log/auth.log

Q212:  How  do  you  lock  a  user  account?

Answer:

sudo  passwd  -l  <username>

Q213:  How  do  you  verify  the  integrity  of  a  backup  file?

●  Answer:

Generate  a  checksum:

md5sum  backup.tar.gz

1.  Compare  it  with  the  original  checksum.
## Page 59

Q214:  How  do  you  back  up  a  MySQL  database  with  compression?

Answer:

mysqldump  -u  root  -p  database_name  |  gzip  >  backup.sql.gz

Q215:  How  do  you  set  up  log  rotation  for  custom  application  logs?

●  Answer:

Create  a  custom  configuration  file:

sudo  vi  /etc/logrotate.d/custom_app   Add:

/var/log/custom_app/*.log  {      daily      rotate  7      compress      missingok      notifempty  }

Q216:  How  do  you  clear  logs  securely?

Answer:

sudo  shred  -u  /var/log/<logfile>

Q217:  How  do  you  view  active  IRQs  in  Linux?

## Page 60

Answer:

cat  /proc/interrupts

Q218:  How  do  you  list  the  system’s  block  devices?

Answer:

lsblk

Q219:  How  do  you  downgrade  a  package  in  Ubuntu?

Answer:

sudo  apt-get  install  <package_name>=<version>

Q220:  How  do  you  check  the  changelog  of  an  installed  package?

Answer:

apt  changelog  <package_name>

Q221:  How  do  you  start  a  VM  using  virsh?

Answer:

virsh  start  <vm_name>

Q222:  How  do  you  display  the  console  output  of  a  VM?

Answer:

virsh  console  <vm_name>

## Page 61

Q223:  How  do  you  view  resource  usage  of  a  Kubernetes  pod?

Answer:

kubectl  top  pod  <pod_name>

Q224:  How  do  you  build  a  Docker  image  from  a  Dockerfile?

Answer:

docker  build  -t  <image_name>:<tag>  .

Q225:  How  do  you  display  system  architecture?

Answer:

uname  -m

Q226:  How  do  you  display  the  last  reboot  time  of  the  system?

Answer:

who  -b

Q227:  How  do  you  configure  a  VLAN  in  Linux?

Answer:

sudo  ip  link  add  link  eth0  name  eth0.100  type  vlan  id  100  sudo  ip  addr  add  192.168.1.2/24  dev  eth0.100  sudo  ip  link  set  dev  eth0.100  up

Q228:  How  do  you  test  the  MTU  size  of  a  network?

Answer:

## Page 62

ping  -M  do  -s  1472  <destination>

Q229:  Write  a  script  to  monitor  a  process  and  restart  it  if  it  stops.

Answer:

#!/bin/  PROCESS="nginx"  if  !  pgrep  $PROCESS  >  /dev/null;  then      echo  "$PROCESS  is  not  running.  Restarting..."      sudo  systemctl  restart  $PROCESS  fi

Q230:  How  do  you  migrate  data  from  one  disk  to  another?

Answer:

rsync  -av  /source/  /destination/

Q231:  How  do  you  prioritize  a  process  using  nice?

Answer:

nice  -n  10  <command>

Q232:  How  do  you  set  up  incremental  backups  with  rsync?

Answer:

rsync  -av  --link-dest=/previous/backup  /source/  /new/backup/

Q233:  How  do  you  configure  a  Linux  server  as  a  router?

●  Answer:

## Page 63

Enable  IP  forwarding:

sudo  sysctl  -w  net.ipv4.ip_forward=1   Make  it  persistent:

echo  "net.ipv4.ip_forward=1"  |  sudo  tee  -a  /etc/sysctl.conf   Add  routing  rules  using  iptables:

sudo  iptables  -t  nat  -A  POSTROUTING  -o  eth0  -j  MASQUERADE

Q234:  How  do  you  capture  only  HTTP  traffic  using  tcpdump?

Answer:

sudo  tcpdump  -i  eth0  port  80

Q235:  How  do  you  set  a  process  to  run  at  a  specific  nice  level  permanently?

●  Answer:

Use  nice while  starting  the  process:

nice  -n  10  <command>   Use  renice for  running  processes:

renice  10  -p  <PID>

Q236:  How  do  you  restart  all  failed  services?

## Page 64

Answer:

sudo  systemctl  list-units  --failed  |  awk  '{print  $1}'  |

xargs

sudo

systemctl

restart

Q237:  How  do  you  monitor  real-time  system  statistics?

Answer:  Use  the  dstat command:

dstat

●  It  provides  real-time  statistics  for  CPU,  memory,  disk  I/O,  and  more.

Q238:  How  do  you  monitor  user  activity  on  a  Linux  system?

Answer:  Use  the  w command:

w

●  It  shows  logged-in  users  and  their  activity.

Q239:  Write  a  script  to  list  all  files  modified  in  the  last  7  days.

Answer:

#!/bin/  find  $1  -type  f  -mtime  -7

Q240:  Write  a  script  to  backup  logs  and  delete  the  originals  after  backup.

Answer:  #!/bin/  LOG_DIR="/var/log"

## Page 65

BACKUP_DIR="/backup"  mkdir  -p  $BACKUP_DIR  tar  -czf  $BACKUP_DIR/logs_$(date  +%F).tar.gz  $LOG_DIR/*.log  rm  $LOG_DIR/*.log

Q241:  How  do  you  move  a  partition  to  a  new  disk?

●  Answer:

Copy  data  using  dd:

sudo  dd  if=/dev/sdX1  of=/dev/sdY1  bs=64K  conv=noerror,sync

1.  Update  /etc/fstab to  reflect  the  new  disk.
Q242:  How  do  you  defragment  a  filesystem?

●  Answer:

For  ext4 filesystems:

sudo  e4defrag  /path/to/filesystem

Q243:  How  do  you  list  all  open  files  by  a  specific  process?

Answer:

lsof  -p  <PID>

Q244:  How  do  you  block  specific  IP  ranges  using  iptables?

Answer:  sudo  iptables  -A  INPUT  -m  iprange  --src-range

192.168.1.0-192.168.1.255
- j
### Drop

## Page 66

Q245:  How  do  you  create  a  differential  backup  using  rsync?

Answer:  rsync  -av  --compare-dest=/path/to/previous/backup  /source/

/path/to/current/backup/

Q246:  How  do  you  restore  permissions  from  a  backup?

●  Answer:  Use  getfacl and  setfacl:

Backup  permissions:

getfacl  -R  /path/to/directory  >  permissions.acl   Restore  permissions:

setfacl  --restore=permissions.acl

Q247:  How  do  you  filter  logs  for  a  specific  date  range?

Answer:

awk  '/2025-01-20/,/2025-01-21/'  /var/log/syslog

Q248:  How  do  you  monitor  changes  to  a  log  file?

Answer:  Use  tail with  -f:

tail  -f  /var/log/syslog

Q249:  How  do  you  list  all  currently  loaded  kernel  modules  with  their  sizes?

Answer:

## Page 67

lsmod

Q250:  How  do  you  remove  a  kernel  module  that’s  in  use?

●  Answer:

Identify  dependent  processes:

lsmod  |  grep  <module_name>   Stop  dependent  processes  or  unload  dependencies  first:

sudo  modprobe  -r  <module_name>
