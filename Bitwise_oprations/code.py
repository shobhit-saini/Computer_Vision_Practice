# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:53:59 2020

@author: SHOBHIT SAINI
"""

import cv2
import numpy as np
img1 = np.zeros((550, 368, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("D:\IIT_BBS_CLG_WORK\IITBBS_LAB_WORK\DF2_lab\Assignment1\white.jpg")
print(img1.shape)
print(img2.shape)

bitAnd = cv2.bitwise_and(img2, img1)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()
