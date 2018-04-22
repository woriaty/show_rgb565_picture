# -*- coding: utf-8 -*-
# !/usr/bin/env python

import cv2
import numpy as np
import time

pix = []
#8位数据前低后高
data_16bit = []

def rgb565_to_rgb888(data):     #rgb565转换为rgb888,并做精度补偿
    r = data>>11
    r = (r<<3)|(r&0x07)
    g = data>>5 & 0x3f
    g = (g<<2)|(g&0x03)
    b = data & 0x1f
    b = (b<<3)|(b&0x07)
    return (b,g,r)

width = 640
height = 100

blank_image = np.zeros((height,width,3), np.uint8)
a = time.time()
print("pix len = %d" % len(pix))
for i in range((len(pix))/2-2):
    # print(i)
    data_16bit.append(pix[i*2+0]<<8 | pix[i*2+1])
#     print(data_16bit)
# print(len(data_16bit))
# print(data_16bit)
for i in range(0,width):
    for j in range(0,height):
        blank_image[j,i] = rgb565_to_rgb888(data_16bit[j*width+i])
b = time.time()
print("time = %fs"%(b-a))
win_name = "camera"
cv2.namedWindow("camera",cv2.WINDOW_AUTOSIZE)
cv2.imshow(win_name, blank_image)
cv2.waitKey()
