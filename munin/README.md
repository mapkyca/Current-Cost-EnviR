Current Cost Munin plugin
==========================
	
This directory contains a plugin for munin <http://munin-monitoring.org/> to monitor the output of a Current Cost EnviR meter.

Usage:
------

 * Install the files from this repo somewhere sensible
 * Link to the file from /etc/munin/plugins as normal
	cd /etc/munin/plugins
	ln -s /path/to/plugins/currentcost_ currentcost_watts
	ln -s /path/to/plugins/currentcost_ currentcost_temp
 * Set an environment variable for 'path' in your plugins settings pointing to the location of current-cost.py (with trailing slash), e.g.

```echo "[currentcost_]
path /path/to/my/plugins/
" > /etc/munin/plugin-conf.d/currentcost
```
 * Restart munin-node

Environment variables:
----------------------

 * path: Configure the location of the current-cost.py script
 * port: Serial port to connect to (default /dev/ttyUSB0)
 * baud: Baud rate (default 57600)

See
---

 * Marcus Povey <http://www.marcus-povey.co.uk>
 * Current Cost <http://www.currentcost.com/>
	 
