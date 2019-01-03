#! usr/bin/python3

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 6:
	msg=raw_input("Enter your message :")
	s.sendto(msg,("127.0.0.1",9999))
	data=s.recvfrom(1000)
print data[0]
