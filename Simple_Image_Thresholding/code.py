# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 05:52:50 2020

@author: SHOBHIT SAINI
"""

import cv2
import numpy as np
img = cv2.imread("D:\\IIT_BBS_CLG_WORK\\CV_Practice\\black.jpg")
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()
