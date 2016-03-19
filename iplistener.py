#!/usr/bin/python

import socketserver
from datetime import datetime
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):

	alarmsender = ""
	bufsize = 4096
	
	def __init__(self, request, client_address, server):
		socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
		return
		
	def logMessage(self, msg, logfile):
		print(msg)

	def handle(self):
		received = ""
		alarmTimestamp = datetime.now()
		self.data = self.request.recv(self.bufsize)
		received = str(self.data)
		recvdata = self.data
		msg = "Message [" + received.strip() + "] received from " + self.client_address[0]
		self.logMessage(str(alarmTimestamp) + " ==> " + msg, logfile)

if __name__ == "__main__":
	HOST, PORT = "", 7200
	# Create the server, binding to localhost on port 9999
	server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
	print("Listening...")
	
	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C or until a server_close()
	# is called
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("Keyboard interrupt received, exiting.")
		server.server_close()
		sys.exit(0)
	finally:
		server.server_close()
		sys.exit(0)