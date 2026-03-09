# Windows

## Collect System Time
- `date /t & time /t`
- `net statistics workstation` --> retrieve system uptime

## Collect Logged-on Users
- `net sessions` --> connection for remote systems
- `net use` --> mapped drives
- `psloggedon.exe` --> not built-in
- `logonsessions.exe` --> not built-in

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
- `promqry` --> not built-in, check promiscuous mode

## Process Information
- `tasklist`
- `Pslist` --> not built-in
- `handle` --> not built-in
- `listdlls` --> not built-in

## Exam Process Memory
- Process Explorer
- `procdump` --> monitor applications for CPU spikes

## Print Spool Files
- buffer for print job
- `.SPL` and `.SHD`
- `C:\Windows\System32\spool\PRINTERS`
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Printers` --> location of spool folder

## Clipboard
- Free Clipboard Viewer
- RecentX

## Service & Driver
- MSInfo32
- `tasklist`
- `wmic service list brief | more`

## Command History
- `doskey /history` --> history will gone after close the terminal windows

## Locally Shared Resources
- `net share`

## File Systems
- `dir /o:d` --> time and date of OS installation (in system32)

## Detect Externally Connected Devices
- DriveLetterView --> From nirsoft
- `devcon listclass usb 1394` --> not built-in

## User Account
- `‪C:\Windows\System32\config\SAM`
- Artifast

## Crash Dump
- DumpChk

## Process Memory
- ProcDump
- Userdump.exe
- adplus.vbs
- Task Manager
- WinDbg --> analyze dump files
- WinHex --> analyze dump files

## Memory Forensics
- Belkasoft RAM Capturer
- FTK Imager
- dd
- Redline --> analyze dump files
- Volatility Framework

## Page File
- Pagefile.sys
- serves as a swap
- `C:\pagefile.sys`
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management`
- DiskExplorer
- FTK Forensic Toolkit
- WinHex --> Open Disk
