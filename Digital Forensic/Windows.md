# Windows

## Collect System Time
- `date /t & time /t`
- `net statistics workstation` --> retrieve system uptime

## Collect Logged-on Users
- `net sessions` --> connection for remote systems
- `net use` --> mapped drives
- `psloggedon.exe` --> 3rd party
- `logonsessions.exe` --> 3rd party

## Collect Open Files
- `net file` --> files accessed

## Collect Network Information
- `nbtstat -c` --> show contents of NetBIOS name cache, which system connected to recently
- `nbtstat -a <IP>` --> asking remote machine to list its NetBIOS Name Table

## Collect Network Connections
- `netstat -naob` --> established network connection
- `netstat -r` --> IP routing table

## Collect Network Status
- `ipconfig /all` --> display network configuration of NICs on the system
- `promqry` --> 3rd party, check promiscuous mode

## Process Information
- `tasklist`
- `Pslist` --> 3rd party
- `handle` --> 3rd party
- `listdlls` --> 3rd party

## Exam Process Memory
- Process Explorer
- `procdump` --> monitor applications for CPU spikes

## Print Spool Files
- buffer for print job
- `.SPL` and `.SHD`
- `C:\Windows\System32\spool\PRINTERS`
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Printers` --> location of spool folder
