import cv2
import numpy as np


# 读取图像
img1 = cv2.imread('lena.png', 0)
img2 = cv2.imread('lena_mirror.png', 0)

# 图像叠加
img = cv2.add(0.5*img1, 0.5*img2)
cv2.imshow('add', np.uint8(img))
cv2.imwrite('img1/add.png', np.uint8(img))


# 图像分离
img = cv2.subtract(np.uint8(img), np.uint8(0.5 * img1))
cv2.imshow('sub', np.uint8(img))
cv2.imwrite('img1/sub.png', np.uint8(img))


# 逻辑运算
mask = np.zeros(img1.shape, dtype='uint8')
mask[10:310, 10:310] += 255
# and
img = cv2.bitwise_and(img1, mask)
cv2.imshow('and', img)
cv2.imwrite('img1/and.png', img)

# or
img = cv2.bitwise_or(img1, mask)
cv2.imshow('or', img)
cv2.imwrite('img1/or.png', img)

# not
img = cv2.bitwise_not(img1)
cv2.imshow('not', img)
cv2.imwrite('img1/not.png', img)

# xor
img = cv2.bitwise_xor(img1, mask)
cv2.imshow('xor', img)
cv2.imwrite('img1/xor.png', img)

# 几何运算
# 按比例缩放
img = cv2.resize(img1, dsize=(0, 0), fx=0.7, fy=0.7)
cv2.imshow('fix_resize_reduce', img)
cv2.imwrite('img1/fix_resize_reduce.png', img)

img = cv2.resize(img1, dsize=(0, 0), fx=1.5, fy=1.5)
cv2.imshow('fix_resize_enlarge', img)
cv2.imwrite('img1/fix_resize_enlarge.png', img)

# 任意缩放
img = cv2.resize(img1, dsize=(300, 500))
cv2.imshow('resize_reduce', img)
cv2.imwrite('img1/resize_reduce.png', img)


img = cv2.resize(img1, dsize=(600, 800))
cv2.imshow('resize_enlarge', img)
cv2.imwrite('img1/resize_enlarge.png', img)
cv2.waitKey(0)
#

