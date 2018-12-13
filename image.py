#!/usr/bin/python3

import cv2


print(cv2.__version__)
img_data=cv2.imread('gaur.jpeg')
#print(img_data)
#print (type(img_data))
new_img_data=img_data-50
cv2.imwrite('gaur1.jpeg',new_img_data)
cv2.imshow('gaur',new_img_data)
cv2.waitKey(0)
cv2.destroyAllWindows()
