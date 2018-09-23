import cv2
import numpy as np


# 盐噪声
def salt(img, n):
    img = img.copy()
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        img[j, i] = 255
    return img


# 椒噪声
def pepper(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        img[j, i] = 0
    return img


raw_img = cv2.imread('lena.png', 0)

# 添加椒盐噪声并与原图像一起显示
img = salt(raw_img, 300)
img = pepper(img, 300)
img = np.hstack((img, raw_img))
cv2.imshow('salt_pepper', img)
cv2.imwrite('img2/salt_pepper.png', img)

# 噪声求平均
img = np.zeros(raw_img.shape)
for i in range(100):
    temp_img = salt(raw_img, 300)
    img += pepper(temp_img, 300)
img = np.uint8(img/100)
cv2.imshow('averge_noise', img)
cv2.imwrite('img2/averge_noise.png', img)

# 图像放大1.5倍
img1 = cv2.resize(img, dsize=(0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('enlarge', img1)
cv2.imwrite('img2/enlarge.png', img1)

# 图像缩小0.8倍
img1 = cv2.resize(img, dsize=(0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_LINEAR)
cv2.imshow('reduce', img1)
cv2.imwrite('img2/reduce.png', img1)

# 图像旋转
matrix = cv2.getRotationMatrix2D((raw_img.shape[1]/2, raw_img.shape[0]/2), -45, 1)
img = cv2.warpAffine(raw_img, matrix, raw_img.shape)
cv2.imshow('rotate', img)
cv2.imwrite('img2/rotate.png', img)

# 最近邻插值
img = cv2.warpAffine(raw_img, matrix, raw_img.shape, flags=cv2.INTER_NEAREST)
cv2.imshow('rotate_nearest', img)
cv2.imwrite('img2/rotate_nearest.png', img)

# 双线性插值
img = cv2.warpAffine(raw_img, matrix, raw_img.shape, flags=cv2.INTER_LINEAR)
cv2.imshow('rotate_linear', img)
cv2.imwrite('img2/rotate_linear.png', img)

# 双三次插值
img = cv2.warpAffine(raw_img, matrix, raw_img.shape, flags=cv2.INTER_CUBIC)
cv2.imshow('rotate_cubic', img)
cv2.imwrite('img2/rotate_cubic.png', img)


cv2.waitKey(0)