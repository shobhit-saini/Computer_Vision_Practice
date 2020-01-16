# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:41:51 2020

"""

import numpy as np
import cv2

img = cv2.imread("D:\IIT_BBS_CLG_WORK\IITBBS_LAB_WORK\DF2_lab\Assignment1\white.jpg")
print(img.shape)#returns a tuple of number of rows, columns and channels
print(img.size)#returns total number of pixels is accessed
print(img.dtype)#returns image datatype is obtained
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

water =img[340:514, 140:198]
print(water.shape)
img[23:197, 159:217] = water
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
