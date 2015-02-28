#!/usr/bin/python

import socket   
import sys
import time


def main():

	## Checking the agruments.
	if(len(sys.argv) < 2) :
		print 'Usage : python knock.py open | close'
		return 1
	if ((sys.argv[1]!='open') and (sys.argv[1]!='close')):
		print 'Usage : python knock.py open | close'
		return 1
	strOp = sys.argv[1]


	strHost = ''  ## Put here the host address you want to connect to.
	intPort1 = 0  ## Specify here the 1st port to knock.
	intPort2 = 0  ## Specify here the 2nd port to knock.
	intPort3 = 0  ## Specify here the 3rd port to knock.


	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error:
		print 'Failed to create socket'
		return 2

	print "Socket Created. Operation: " + strOp


	if(strOp=='open'):
		s.sendto("a", (strHost , intPort1))
		time.sleep(1)
		s.sendto("a", (strHost , intPort2))
		time.sleep(1)
		s.sendto("a", (strHost , intPort3))
		time.sleep(1)
	else:
		s.sendto("a", (strHost , intPort3))
		time.sleep(1)
		s.sendto("a", (strHost , intPort2))
		time.sleep(1)
		s.sendto("a", (strHost , intPort1))
		time.sleep(1)

	print "Message sent"
	return 0




if __name__ == '__main__':
	sys.exit(main())

