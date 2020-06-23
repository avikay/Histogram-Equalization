# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:03:38 2020

@author: Avinash
"""

import cv2
import numpy as np

img = cv2.imread("bnw_image.jpg",0)
equ = cv2.equalizeHist(np.uint8(img))
res = np.hstack((img,equ))
cv2.imwrite('res.png',res)