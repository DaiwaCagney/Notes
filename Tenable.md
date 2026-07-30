# Tenable

## Tenable Manager
- `systemctl start nessusd`
- `systemctl stop nessusd`

## Agent - Ubuntu
- `systemctl stop nessusagent`
- `systemctl start nessusagent`
- `/opt/nessus_agent/sbin/nessuscli agent status`
- `/opt/nessus_agent/sbin/nessuscli bug-report-generator`

### Agent Removal
- `dpkg -r NessusAgent`
- `rm -rf /opt/nessus_agent/`
- `rm -f /etc/tenable_tag`

### Agent Installation
- `dpkg -i “NessusAgent_name”`
- `/opt/nessus_agent/sbin/nessuscli agent prepare-image`
- `/opt/nessus_agent/sbin/nessuscli agent link --key=<linking_key> --host=<manager_host> --port=8834`
