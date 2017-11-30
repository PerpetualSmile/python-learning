import cv2
import numpy as np
sigma = 1


if __name__ == '__main__':
    img = cv2.imread("5.jpg", 0)
    cv2.imshow('raw', img)
    cv2.waitKey(1)
    # 空域平滑

        # 高斯滤波
    kernel = cv2.getGaussianKernel(5, sigma)
    Gaussian_img = cv2.sepFilter2D(img, -1, kernel, kernel)
    cv2.imwrite('Guassian.jpg', Gaussian_img)
    # cv2.imshow('Gaussian', Gaussian_img)
    cv2.waitKey(1)

        # 均值滤波
    Normalized_img = cv2.blur(img, (5, 5))
    cv2.imwrite('Normalized.jpg', Normalized_img)
    # cv2.imshow('Normalized', Normalized_img)
    cv2.waitKey(1)

        # 中值滤波
    median = cv2.medianBlur(img, 5)
    cv2.imwrite('Median.jpg', median)
    # cv2.imshow('Median', median)
    cv2.waitKey(1)

    # 空域锐化

        # Laplace
    Laplace = cv2.Laplacian(img, -1, ksize=3)
    cv2.imwrite('Laplace.jpg', Laplace)
    cv2.imshow('Laplace', Laplace)
    cv2.waitKey(1)

        # Sobel
    Sobel = cv2.Sobel(img, -1, 1, 1, ksize=3)
    cv2.imwrite('Sobel.jpg', Sobel)
    cv2.imshow('Sobel', Sobel)
    cv2.waitKey(1)

        # Prewitt
    filter1 = np.array([1, 1, 1, 0, 0, 0, -1, -1, -1]).reshape(3, 3)
    filter2 = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1]).reshape(3, 3)
    p1 = cv2.filter2D(img, -1, filter1)
    p2 = cv2.filter2D(img, -1, filter2)
    Prewitt = cv2.add(p1, p2)
    cv2.imwrite('Prewitt.jpg', Prewitt)
    cv2.imshow('Prweitt', Prewitt)
    cv2.waitKey(1)

    # 频域平滑

        # 低通滤波
    mask = np.zeros(img.shape, dtype=np.uint8)
    r = int(img.shape[0]/2)
    c = int(img.shape[1] / 2)

    radius = 150
    mask[r - radius:r + radius, c - radius:c + radius] = 1
    f1 = np.fft.fft2(img)
    f1shift = np.fft.fftshift(f1)
    f1shift *= mask
    f2shift = np.fft.ifftshift(f1shift)
    img_new = np.fft.ifft2(f2shift)
    # 出来的是复数，无法显示
    img_new = np.abs(img_new)
    # 调整大小范围便于显示
    low_pass = (img_new - np.amin(img_new)) / (np.amax(img_new) - np.amin(img_new))
    cv2.imwrite('Low_pass.jpg', low_pass * 256)
    cv2.imshow('Low_pass', low_pass)
    cv2.waitKey(1)

    # 频域锐化

        # 高通滤波
    mask = np.zeros(img.shape, dtype=np.uint8) + 1
    r = int(img.shape[0] / 2)
    c = int(img.shape[1] / 2)

    radius = 150
    mask[r - radius:r + radius, c - radius:c + radius] = 0
    f1 = np.fft.fft2(img)
    f1shift = np.fft.fftshift(f1)
    f1shift *= mask
    f2shift = np.fft.ifftshift(f1shift)
    img_new = np.fft.ifft2(f2shift)
    # 出来的是复数，无法显示
    img_new = np.abs(img_new)
    # 调整大小范围便于显示
    high_pass = (img_new - np.amin(img_new)) / (np.amax(img_new) - np.amin(img_new))
    cv2.imwrite('High_pass.jpg', high_pass * 256)
    cv2.imshow('High_pass', high_pass)
    cv2.waitKey(1)

    # 图像清晰化
    T = 30
    img_new = img.copy()
    width, height = img.shape
    for i in range(width - 1):
        for j in range(height - 1):
            G = abs(img[i + 1, j] - img[i, j]) + abs(img[i, j + 1] - img[i, j])
            if G >= 30:
                img_new[i, j] = T
            else:
                img_new[i, j] = img[i, j]
    cv2.imwrite('Gradient_sharp.jpg', img_new)
    cv2.imshow('Gradient_sharp', img_new)
    cv2.waitKey(1)

    # 二值化梯度图
    threshold = 80
    img_new = img.copy()
    width, height = img.shape
    for i in range(width - 1):
        for j in range(height - 1):
            if img[i, j] >= threshold:
                img_new[i, j] = 255
            else:
                img_new[i, j] = 0
    cv2.imwrite('Two_value.jpg', img_new)
    cv2.imshow('Two_value', img_new)
    cv2.waitKey(1)

    cv2.waitKey(0)