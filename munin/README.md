Weather Display Munin plugin
============================
	
This directory contains a number of plugins for munin <http://munin-monitoring.org/> to monitor various stats produced by the "Weather Display" weather station software, using the wd-parse.py program.

Usage:
------

 * Copy the files to your munin plugin installation directory and configure the path to wd-parse.py within the files (later, I'll do this via an environment variable, but these are just quick hacks at the moment!)
 * Link to the file from /etc/munin/plugins as normal, specifying the root URL of the weather station after the underscore, so for example, to monitor the wind speed at my local aerodrome, you'd do the following:

	cd /etc/munin/plugins
	ln -s /path/to/wd/plugins/wdwind_ wdwind_www.enstoneaerodrome.co.uk
 * Restart munin-node

Limitations:
------------

 * The script expects to find clientraw.txt in the root directory of the domain requested, I'll add more flexibility in future versions.
	
See
---

 * Marcus Povey <http://www.marcus-povey.co.uk>
 * Weather Display <http://www.weather-display.com/index.php>
	 
