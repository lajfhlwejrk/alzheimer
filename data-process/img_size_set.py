import cv2
import glob
img_path = glob.glob(r"/home/haotian/ad_nc_classification_orchid/dataset/train_src/PET/*/*.png")
size_set = set()
for i in img_path:
    img = cv2.imread(i)
    size_set.add(img.shape[:2])
print(size_set)