"""
@author: SHOBHIT
"""

import cv2
import numpy as np
import pandas as pd
img = cv2.imread("D:\IIT_BBS_CLG_WORK\IITBBS_LAB_WORK\DF2_lab\white.jpg")
print(img)
cv2.imshow("ab",img)
num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1,0,100], [0, 1, 200]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols+100, num_rows+200))
cv2.imshow("abc",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
