Current Cost EnviR reader tool
==============================

This is a simple command line tool for fetching the current energy usage, temperature and time from a Current Cost EnviR electricity usage meter.

It has been tested against the EnviR meter, but may well work with other meters in the current cost range.
	
Usage:
------
	
	python current-cost.py [-t timeout] [-p serial-port] [-b baudrate] [-o "formatted list of output"]

Where:

 * timeout: is max time to wait for a reading (Default 10 seconds)
 * serial-port: Serial port that the meter is connected to (default /dev/ttyUSB0)
 * baudrate: Speed to connect to device (default 57600, which you shouldn't need to change unless you're using a different meter)

Format string similar to 'Energy Now: {{option}}, Temperature: {{option}}'

See
===

 * Marcus Povey <http://www.marcus-povey.co.uk>
 * Current Cost <http://www.currentcost.com/>
	 
