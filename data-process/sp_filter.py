# coding=utf-8
# 中值滤波，针对椒盐噪声，src_dir是原图像路径，dst_dir是修改后图像路径
import cv2
import numpy as np
import os
src_dir = "/home/haotian/ad_nc_classification_orchid/dataset/train/PET/NC/"
dst_dir = "/home/haotian/ad_nc_classification_orchid/dataset/train_med/PET/NC/"
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
src_list = os.listdir(src_dir)
i = 0
for img in src_list:
    i = i+1
    src = cv2.imread(src_dir + img)
    dst = cv2.medianBlur(src,3)
    cv2.imwrite(dst_dir + img,dst)
