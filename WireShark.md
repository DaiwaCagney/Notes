# WireShark

## Display Filter:
`http`

`ip.addr == 192.168.1.1`

`tcp.port == 443`

`http contains "hack"`

`(not tcp.port == 80 and not tcp.port == 8080) and http contains "hack"`

`dns.flags.response == 1 and dns.count.answers > 5 and dns.qry.name contains "drive.io"`

`http.cookie matches "(?i)dean"`

`http.response.code in {200 301 302 404}`

`dns.qry.name == "www.cyberengage.org"`

`dns.a != 192.168.1.1 --> dns.a && !(dns.a == 192.168.1.1)`

`ip.addr==192.168.1.100 && tcp.port==23`

`ip.addr==192.168.1.100 or ip.addr==192.168.1.101`

`ip.dst==192.168.1.100 && ip.src==192.168.1.101`

`ip.dst==192.168.1.100 && frame.pkt_len > 400`

`ip.dst==192.168.1.100 && icmp && frame.number > 15`

## SYN-FIN Flood:
`tcp.flags==0x003`

## ICMP Flood:
`icmp.type==8`

## UDP Flood:
`(ip.proto==17)&&(udp.dstport==80)`

## Http Flood:
`tcp.stream eq 1`

## FTP Password Cracking:
`ftp.response.code==530` --> failed login

`ftp.response.code==230` --> successful login

## Notes:
By default, Wireshark disables DNS lookups

Never turn on “Use an external network name resolver” if you care about stealth

Instead, use “Use captured DNS packet data for address resolution” This resolves hostnames from the DNS packets in the capture, no external traffic

Timestamps in the packet metadata (in the pcap) are in UTC. But any timestamps inside the packet data (like HTTP headers or app logs) can be in any timezone
