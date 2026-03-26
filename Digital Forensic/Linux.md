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
