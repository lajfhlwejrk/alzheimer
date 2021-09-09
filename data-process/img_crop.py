import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

def second(img, new_path):
    img = np.array(img)
    dowm = img.shape[0]
    up = img.shape[1]
    max1 = max(dowm, up)
    dowm = (max1 - dowm) // 2
    up = (max1 - up) // 2
    dowm_zuo, dowm_you = dowm, dowm
    up_zuo, up_you = up, up
    if (max1 - img.shape[0]) % 2 != 0:
        dowm_zuo = dowm_zuo + 1
    if (max1 - img.shape[1]) % 2 != 0:
        up_zuo = up_zuo + 1
    matrix_pad = np.pad(img, pad_width=((dowm_zuo, dowm_you),  # 向上填充1个维度，向下填充两个维度
                                        (up_zuo, up_you),  # 向左填充2个维度，向右填充一个维度
                                        (0, 0))  # 通道数不填充
                        , mode="constant",  # 填充模式
                        constant_values=(0, 0))  # 第一个维度（就是向上和向左）填充6，第二个维度（向下和向右）填充5
    img = Image.fromarray(matrix_pad)
    img.save(new_path)


def first(path, save_path):  # 第一次裁剪大脑
    i = 0
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for file in os.listdir(path):
        i += 1
        file_path = os.path.join(path, file)
        new_path = os.path.join(save_path, file)
        img = Image.open(file_path).convert('RGB')
        img = np.array(img)
        index = np.where(img > 50)  # 找出像素值大于50的所以像素值的坐标
        x = index[0]
        y = index[1]
        max_x = max(x)
        min_x = min(x)
        max_y = max(y)
        min_y = min(y)
        max_x = max_x + 10
        min_x = min_x - 10
        max_y = max_y + 10
        min_y = min_y - 10
        if max_x > img.shape[0]:
            max_x = img.shape[0]
        if min_x < 0:
            min_x = 0
        if max_y > img.shape[1]:
            max_y = img.shape[1]
        if min_y < 0:
            min_y = 0
        img = Image.fromarray(img[min_x:max_x, min_y:max_y, :])
        second(img, new_path)


if __name__ == '__main__':
    path = r'/home/haotian/ad_nc_classification_orchid/dataset/val_mri' 
    save_path = r'/home/haotian/ad_nc_classification_orchid/dataset/val_MRI'
    first(path, save_path)