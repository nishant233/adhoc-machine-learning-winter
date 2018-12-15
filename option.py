#! usr/bin/env python
import webbrowser
import time

menu='''
Press 1 to google search
Press 2 to get the URLs
Press 3 to googe  images
Press 4 to check current logged in user
Press 5 to logout your system graphically
Press 6 to login to facebook accoun
Press 7 to send email to someone
Press 8 to list all connected ip and mac to your curreent network
Press 9 to check the number of tabs in your web browser 
'''
print menu
ch=raw_input("Enter your option")

if(ch=='1'):
	get_data=raw_input('Enter anything')
	final_data=get_data.strip().split()
	print final_data
	for i in final_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)


if(ch=='3'):
        get_data=raw_input('Enter anything')
        final_data=get_data.strip().split()
        print final_data
        for i in final_data:
		webbrowser.open_new_tab("https://www.images.google.com/search?q="+i)
