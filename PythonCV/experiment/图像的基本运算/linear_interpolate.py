import cv2
import numpy as np


def linear_interpolate(img, m, n):
    m = int(m)
    n = int(n)
    height, width, channels = img.shape
    result_image = np.zeros((m, n, channels), dtype='uint8')
    value = [0, 0, 0]
    sh = m/height
    sw = n/width
    for i in range(m):
        for j in range(n):
            # x,y为坐标反变换之后对应的整数值
            x = int(i//sh)
            y = int(j//sw)
            # P、Q为浮点数部分
            p = i/sh-x
            q = j/sw-y
            for k in range(3):
                # 防止反变换之后越界
                if x+1 < height and y+1 < width:
                    # 运用公式计算像素值
                    value[k] = int(img[x, y][k]*(1-p)*(1-q)+img[x, y+1][k]*q*(1-p)+img[x+1, y][k]*(1-q)*p + img[x+1, y+1][k] * p * q)
            result_image[i, j] = (value[0], value[1], value[2])
    return result_image

img = cv2.imread("lena.png")
img = linear_interpolate(img, img.shape[0]*2.4, img.shape[1]*2.4)
cv2.imshow("Bilinear_Interpolation", img)
cv2.imwrite("Bilinear_Interpolation.png", img)
cv2.waitKey(0)