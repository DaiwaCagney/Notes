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
