# Linux

## Manual
- `man man`
- `man netstat`

## Hostname, Date and Time
- `hostname`
- `date`
- `cat /etc/timezone`
- `date +%s` --> epoch timestamp

## Uptime
- `uptime`
- `top`

## Network
- `ip addr show`
- `netstat`
- `ifconfig`

## Routing Table
- `netstat -rn`
- `ip r`

## Open Port
- `nmap -sT localhost` --> TCP
- `nmap -sU localhost` --> UDP

## Process associated with Port
- `netstat -tulpn`
- `lsof -i -P -n | grep LISTEN`

## Open Files and Mounted File System
- `lsof | more`
- `mount`
- `df`

## Loaded Kernel Modules
- `lsmod`
- `modinfo <kernel_module>`

## Running Processes
- `ps -aux`
- `ps auxww`

## Services
- `systemctl list-units --type=service -all`
- `systemctl --type=service -state=<state>`
- `systemctl --type=service -state=<state1>,<state2>`
- `systemctl --type=service -state=<state> | grep <service_type>`

## Disk Partition and Swap Areas
- `cat /proc/swaps`
- `cat /proc/partitions`

## Kernel Message
- `dmesg`

## System Information
- `cat /proc/cpuinfo`
- `cat /proc/self/mounts` --> mount points and mounted external devices

## User Account
- `cat /etc/passwd`
- `cut -d: -f1 /etc/passwd`

## Logged-in Users and Login History
- `w` --> logged-in users
- `last`
- `last -f /var/log/wtmp` --> login history, system reboot time, system status
- `cat /var/log/auth.log`
- `grep sudo /var/log/auth.log` --> execution of sudo command

## System Log
- `cat /var/log/syslog`
- `cat /var/log/kern.log`

## Command History
- `history`
- `history -c` -->  clear history

## Hidden Files
- `ls -al`

## Rootkit
- `rkhunter --check --rwo`
- `chkrootkit`

## File Signature
- `xxd image.png | head`
- `xxd document.pdf | head`
- `file document.pdf`
- `strings document.pdf`
- `strings -t d Evidence.dd | grep -iE "kitty"`

## Find Writable Files
- `find / -writable -type f 2>/dev/null | grep "/var/log"`

## Cron Jobs
- `sudo systemctl status cron` --> check Cron service running
- `grep CRON /var/log/syslog` --> view Cron logs
- `crontab -l`
- `sudo crontab -u [username] -l`

## Hash
- `md5sum filename`

## Volatility
- `python3 vol.py -f Linux.mem linux.lsof`
- `python3 vol.py -f Linux.mem linux.mount`
- `python3 vol.py -f Linux.mem linux.bash`
- `python3 vol.py -f Linux.mem linux.lsmod`
- `python3 vol.py -f Linux.mem linux.pslist`
- `python3 vol.py -f Linux.mem linux.psscan`
- `python3 vol.py -f Linux.mem linux.malfind`
