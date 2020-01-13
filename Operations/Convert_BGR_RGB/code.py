# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 01:14:25 2020

@author: SHOBHIT SAINI
"""
import numpy as np
import cv2 
# Import the image
img = cv2.imread('D:\IIT_BBS_CLG_WORK\CV_Practice\island.jpeg')
cv2.imshow('BGR_img_default', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB_IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
