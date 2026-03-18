# Windows

## Collect System Time
- `date /t & time /t`
- `net statistics workstation` --> retrieve system uptime

## Collect Logged-on Users
- `net sessions` --> connection for remote systems
- `net use` --> mapped drives
- `psloggedon.exe`
- `logonsessions.exe`

## Collect Open Files
- `net file` --> files accessed
- `NetworkOpenedFiles.exe`

## Collect Network Information
- `nbtstat -c` --> show contents of NetBIOS name cache, which system connected to recently
- `nbtstat -a <IP>` --> asking remote machine to list its NetBIOS Name Table

## Collect Network Connections
- `netstat -ano`
- `netstat -naob` --> established network connection
- `netstat -r` --> IP routing table

## Collect Network Status
- `ipconfig /all` --> display network configuration of NICs on the system
- `promqry` --> check promiscuous mode

## Process Information
- `tasklist`
- `Pslist`
- `handle`
- `listdlls`

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
- `devcon listclass usb 1394`

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

## Hibernate File
- snapshot of RAM data created when system hibernates
- hiberfil.sys
- Hex Editor
- AccessData FTK Imager
- MoonSols Windows Memory Toolkit

## MemProcsFS
- `MemProcsFS.exe -device <path of memory dump file> -forensic 1`

## USB Removable Storage Devices
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR`

## Start Up
- Autoruns
- Autorunsc

## UserAssist Keys
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{GUID}\Count`
- ROT13 encryption

## MRU Lists
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU`
- `HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\TypedURLs`
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts`

## Connect to other system
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Map Network Drive MRU`
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2`

## Webcam and Microphone
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone`
- `HKEY_USERS\<UserName>\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam`
- `HKEY_USERS\<UserName>\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone`

## Google Chrome
- `C:\Users\<UserName>\AppData\Local\Google\Chrome\User Data\Default` --> history, downloads, cache
- `C:\Users\<UserName>\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies`
- ChromeHistoryView
- ChromeCacheView
- ChromeCookiesView
- `ipconfig/displaydns` --> DNS cache

## Prefetch Files
- WinPrefetchView
- Windows Prefetch Parser

## Image
- Exiv2
- IrfanView
- ExifTool
- Exif Pilot
- Exif Library

## Metadata
- Metadata++

## Metadata in PDF
- Adobe Acrobat
- ExifTool

## ShellBags
- ShellBagsView
- TZWorks Windows ShellBag Parser
- FTK Forensic Toolkit

## LNK Files
- `C:\Users\<UserName>\AppData\Roaming\Microsoft\Windows\Recent`

## Jump List
- `C:\Users\<UserName>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations`
- `C:\Users\<UserName>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations`
- JumpListsView

## Event Logs
- `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog` --> Configuration
- `wevtutil`
- `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet00<x>\Services\EventLog\<log name>`
- secpol.msc
- Microsoft Log Parser
- `C:\Windows\System32\winevt\Logs`

## Using of Strings in Linux
- `strings Windows_RAM.mem | grep -i "^[a-z]:\\\\" | sort | uniq`
- `strings Windows_RAM.mem | egrep "^https?://" | sort | uniq`
- `strings Windows_RAM.mem | egrep "172.20.20.10"`
