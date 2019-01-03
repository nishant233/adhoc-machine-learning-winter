#! usr/bin/python3

import os
while 6:
	ch=input("Enter a word or enter exit to exit:")
	check=os.system(ch)
	if ch=="exit":
		exit()
	elif check==0:
		print("this is a command")
	else:
		print("This is not a command")
