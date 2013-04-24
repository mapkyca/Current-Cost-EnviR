#!/usr/bin/python
###
# current-cost.py
#
# This is a simple tool for reading the latest values from a current cost energy
# meter. This works with my Current Cost EnviR, but it might work with other
# meters in the range.
# 
# @author Marcus Povey <marcus@marcus-povey.co.uk>
# @copyright Marcus Povey 2013
# @link http://www.marcus-povey.co.uk
# 
# Copyright (c) 2013 Marcus Povey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###

import getopt
import sys
import serial
import re

def usage():
	print("Current-Cost v1.0 By Marcus Povey <marcus@marcus-povey.co.uk>");
	print
	print("Usage: python current-cost.py [-t timeout] [-p serial-port] [-b baudrate] [-o \"formatted list of output\"]")
	print
	print("Where:")
	print("\t * timeout: is max time to wait for a reading (Default 10)")
	print("\t * serial-port: Serial port that the meter is connected to (default /dev/ttyUSB0)")
	print("\t * baudrate: Speed to connect to device (default 57600, which you shouldn't need to change unless you're using a different meter)")
	print
	print("Format string similar to 'Energy Now: {{option}}, Temperature: {{option}}'")
	print
	print("Where option can be {{watts}}, {{temp}}, {{time}}")

def main():
	
	port = '/dev/ttyUSB0'
	baud = 57600
	timeout = 10
	format = "Energy Usage at {{time}}: {{watts}} watts, room temperature {{temp}}C"

	try:
		opts, args = getopt.getopt(sys.argv[1:], "t:p:b:o:h", ["help"])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit()

	for o, a in opts:
		if o == "-t":
			timeout = int(a)
		elif o == "-p":
			port = a
		elif o == "-b":
			baud = int(a)
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o == "-o":
			format = a
		else:
			usage()
			sys.exit()
			
			
			
	meter = serial.Serial(port, baud, timeout=timeout)
	meter.open()
	
	data = meter.readline()
	
	meter.close()
	
	watts_ex = re.compile('<watts>([0-9]+)</watts>')
	temp_ex = re.compile('<tmpr>([0-9\.]+)</tmpr>')
	time_ex = re.compile('<time>([0-9\.\:]+)</time>')
	
	watts = str(int(watts_ex.findall(data)[0])) # cast to and from int to strip leading zeros
	temp = temp_ex.findall(data)[0]
	time = time_ex.findall(data)[0]
	
	# Replace format string
	format = format.replace("{{watts}}", watts)
	format = format.replace("{{time}}", time)
	format = format.replace("{{temp}}", temp)
	
	print format
	
if __name__ == "__main__":
    main()
