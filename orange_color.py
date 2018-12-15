#!/usr/bin/python3

import cv2

# start camera
cap=cv2.VideoCapture(0)

while True:

	status,frame=cap.read()
	# capture only red frame
	orange_img=cv2.inRange(frame,(0,0,0),(0,215,255))
	cv2.imshow('orangewindow',orange_img)
	print(frame)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()
cap.release()
