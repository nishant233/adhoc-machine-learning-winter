#!/usr/bin/python3

import cv2
import os

#classifing xml file
cascade=cv2.CascadeClassifier("face.xml")

ctr=0

#starting camera
camera=cv2.VideoCapture(0)

#defining directory name where images will be stored
directory="/home/nishant/Desktop/adhoc-machine-learning-winter/images/"

#using try to avoid error when directory is already present
try:
	os.mkdir(directory)
except:
	print()

while camera.isOpened():

	frame=camera.read()[1]     #reading the frame
	gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)       #taking gray images
	faces=cascade.detectMultiScale(gray_image,1.5,5)        #detecting faces in gray frame
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)         #rectangle around the face
		ctr=ctr+1
		print(ctr)
		cv2.imwrite(directory+"/image"+str(ctr)+".jpg",gray_image)      #saving the image
	print("Image saved!")

	if cv2.waitKey(0) & 0xFF==ord('q'):
		break
	elif cv2.waitKey(0) & counter==15:
		break
camera.release()
cv2.destroyAllWindows()
