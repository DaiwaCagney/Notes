# Splunk

## System Related
Alert:  
- `| rest /servicesNS/-/-/saved/searches | table title, search`

Index:  
- `| eventcount summarize=false index=* index=_* | dedup index | fields index`

Forwarder:  
- `index=_internal source=*metrics.log group=tcpin_connections | dedup hostname | table Hostname, SourceIP, OS`

Error:  
- `index=_internal source="*/splunkd.log"`

## Query
- `| search ({ } = { } AND { } != { })`
- `| search NOT ({ }={ })`
- `| where { } > { } OR ({ } > { } AND { } > { })`
- `| stats values({ }) as { }, dc({ }) as { }, count as Total, by { }`
- `| stats Median(count) as { } by { }`
- `| join type=left [search ... earliest=-8h@h latest=-1h@h]`
- `| bucket _time span=1h`
- `| eval { }=if(isnotnull({ }),{ },{ })`
- `| rename { } as { }`
- `| dedup { }`
- `| table { },{ },{ },{ }`
- `| timechart span=1w count by { } limit=5`
- `| eval time=tostring(filed_with_seconds, "duration")`
- `| sort { } -{}`
- `| rex field=_raw "(?<ts_epoch>\d+\.\d+)\s+(?<uid>\S+)\s+(?<src_ip>\d+\.\d+\.\d+\.\d+)\s+(?<src_port>\d+)\s+(?<dst_ip>\d+\.\d+\.\d+\.\d+)\s+(?<dst_port>\d+)\s+(?<result>\S+)\s+(?<direction>\S+)\s+(?<client_version>\S+)\s+(?<server_version>\S+)"`
- `| eval timestamp = strftime(ts_epoch, "%Y-%m-%d %H:%M:%S")`
- `| regex _raw="(?i)\b(ssh|domain|query|response|port 22)\b"`
- `| rex field=_raw "^(?<ts_epoch>\d+\.\d+)\\t(?<uid>\\S+)\\t(?<src_ip>[^\\t]+)\\t(?<src_port>\\d+)\\t(?<dst_ip>[^\\t]+)\\t(?<dst_port>\\d+)\\t(?<result>\\S+)"`
- `| timechart span=5m count(eval(result="failure")) AS failures`
- `NOT ip_address="10.10.*.*"`

## Path
/opt/splunk/etc/deployment-apps/

## Command
/opt/splunk/bin/splunk restart

## Detect Ransomware
```
sourcetype="xmlwineventlog:microsoft-windows-sysmon/operational" EventDescription="File Create Time"
| streamstats time_window=1m count(EventDescription) AS "new_files"
| search new_files>10
```

## Routing data to the nullQueue
1. Define Sourcetype and Keyword that want to drop
2. Create the Rule in transforms.conf
  - `cd /opt/splunk/etc/system/local/`
  - `vi transforms.conf`
```
[drop_button_clicks]
REGEX = DEBUG: User clicked button
DEST_KEY = queue
FORMAT = nullQueue
```
  - `[drop_button_clicks]` --> rule name
  - `DEST_KEY = queue` and `FORMAT = nullQueue` --> Standard for "send this data to the trash"
3. Apply the Rule to your Data in props.conf
  - `vi props.conf`
```
[app_error_log]
TRANSFORMS-trash_clicks = drop_button_clicks
```
  - `[app_error_log]` --> sourcetype that want to filter
  - `TRANSFORMS-trash_clicks` --> This tells Splunk to apply a transform rule. The word after the hyphen (trash_clicks) is just a unique label. You can name it `TRANSFORMS-anything`
4. Restart Splunk
  - `/opt/splunk/bin/splunk restart`
