import cv2
import os
import numpy as np
import random

img_src_dir = "/home/haotian/ad_nc_classification_orchid/dataset/train/PET/AD/" 
img_dst_dir = "/home/haotian/ad_nc_classification_orchid/dataset/train/PET/AD/" 
img_files = os.listdir(img_src_dir)


def imgBrightness(img1, c, b): 
    rows, cols, channels = img1.shape
    blank = np.zeros([rows, cols, channels], img1.dtype)
    rst = cv2.addWeighted(img1, c, blank, 1-c, b)
    return rst

for img_src_file in img_files:
    img_src_str = img_src_file.replace('.png','')
    img_src = cv2.imread(img_src_dir + img_src_file)

    img_lr = np.fliplr(img_src)
    img_ud = np.flipud(img_src)
    img_f180 = np.flipud(img_lr)
    bU = random.randint(100,180)/100
    bD = random.randint(50,100)/100
    img_lightU = imgBrightness(img_src, bU, 0)
    img_lightD = imgBrightness(img_src, bD, 0)

    img_lr_file = img_src_str + '_lr.png'
    img_ud_file = img_src_str + '_ud.png'
    img_f180_file = img_src_str + '_f180.png'
    img_lightU_file = img_src_str + '_lightU.png'
    img_lightD_file = img_src_str + '_lightD.png'

    cv2.imwrite(img_dst_dir + img_lr_file,img_lr)
    cv2.imwrite(img_dst_dir + img_ud_file,img_ud)
    cv2.imwrite(img_dst_dir + img_f180_file,img_f180)
    cv2.imwrite(img_dst_dir + img_lightU_file,img_lightU)
    cv2.imwrite(img_dst_dir + img_lightD_file,img_lightD)