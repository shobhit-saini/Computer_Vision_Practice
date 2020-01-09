"""
@author: SHOBHIT SAINI
"""

import cv2
import numpy as np
import pandas as pd
img = cv2.imread("D:\IIT_BBS_CLG_WORK\IITBBS_LAB_WORK\DF2_lab\white.jpg")
print(img)
flip_vertical = cv2.flip(img, 0)
flip_horizontal = cv2.flip(img, 1)
flip_both = cv2.flip(img, -1)
cv2.imshow('original', img)
cv2.imshow('vertical', flip_vertical)
cv2.imshow('horizontal', flip_horizontal)
cv2.imshow('both', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
