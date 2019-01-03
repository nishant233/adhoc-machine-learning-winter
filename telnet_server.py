#! usr/bin/python3	
import socket
myip="127.0.0.1"
myport=9999

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((myip,myport))
while 4:
	data=s.recvfrom(1000)
	print data[0]
	r=raw_input('type to reply ')
s.sendto(r,data[1])
