# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 02:05:01 2020

@author: SHOBHIT SAINI
"""

import numpy as np
import cv2
img = cv2.imread('D:\IIT_BBS_CLG_WORK\IITBBS_LAB_WORK\DF2_lab\Assignment1\white.jpg')
img = cv2.line(img, (0,0), (255,255),(140, 98, 22), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'openCv', (5, 200),font, 4, (10, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
