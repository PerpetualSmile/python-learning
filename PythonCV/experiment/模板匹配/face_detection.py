import cv2
import numpy as np
sigma = 1


def conv2D(img, kernel):
    w, h = kernel.shape
    sum = 0
    for i in range(w):
        for j in range(h):
            sum = sum + (img[i, j] * kernel[i, j])
    return sum


# 逐个像素点卷积计算
def myGaussfilter(img, kernel):
    w, h = img.shape
    wk, hk = kernel.shape
    posi = int((wk - 1) / 2)
    posj = int((wk - 1) / 2)
    for i in range(posi, w - posi):
        for j in range(posj, h - posj):
            img[i, j] = conv2D(img[i - posi:i + posi + 1, j - posj: j + posj + 1], kernel)/273


def myMatchTemplate(img, template, n):
    img = np.int64(img)
    template = np.int64(template)
    w = template.shape
    width, height = img.shape
    res = np.zeros((width - w[0], height - w[1]))
    for i in range(0, width - w[0]):
        for j in range(0, height - w[1]):
            window = img[i:i+w[0], j:j+w[1]]
            res[i, j] = similarity_cal(window, template, n)
    return res


# 相似度计算
def similarity_cal(window, template, n):
    # 平方差匹配
    if 0 == n:
        return np.sum(np.square(window - template))

    # 标准平方差匹配
    if 1 == n:
        return np.sum(np.square(window - template))/np.sqrt(np.sum(np.square(window))*np.sum(np.square(template)))

    # 相关匹配CCORR
    if 2 == n:
        return np.sum(window * template)

    # 标准相关匹配CCORR
    if 3 == n:
        return np.sum(window * template)/np.sqrt(np.sum(np.square(window))*np.sum(np.square(template)))

    # 相关匹配CCOEFF
    if 4 == n:
        window_ = window - np.sum(window)/window.size
        template_ = template - np.sum(template) / template.size
        return np.sum(window_ * template_)

    # 标准相关匹配
    if 5 == n:
        window_ = window - np.sum(window) / window.size
        template_ = template - np.sum(template) / template.size
        return np.sum(window_ * template_)/np.sqrt(np.sum(np.square(window_))*np.sum(np.square(template_)))


if __name__ == '__main__':
    img = cv2.imread("raw_image.jpg", 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 逐个像素点卷积处理 + 自定义的模板匹配实现
    img_gray1 = img_gray.copy()
    template = cv2.imread('template_image.jpg', 0)
    GaussKernel = np.array([1, 4, 7, 4, 1, 4, 16, 26, 16, 4, 7, 26 ,41 ,26, 7, 4, 16, 26, 16, 4, 1, 4, 7, 4, 1]).reshape(5, 5)
    myGaussfilter(img_gray1, GaussKernel)
    cv2.imwrite('custom_1.jpg', img_gray1)
    cv2.imshow('customFilter', img_gray1)
    cv2.waitKey(1)
    # 自定义模板匹配
    res = myMatchTemplate(img_gray1, template, 4)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = max_loc
    img1 = img.copy()
    cv2.rectangle(img1, max_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.rectangle(img_gray1, max_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.imwrite('custom_2.jpg', img_gray1)
    cv2.imshow('custom_myMatchTemplate', img1)
    cv2.imwrite('custom_3.jpg', img1)
    cv2.waitKey(1)


    # 使用filter2D函数滤波处理
    img_gray2 = img_gray.copy()
    kernel = np.array(
        [[0.0751136, 0.123841, 0.0751136], [0.123841, 0.20418, 0.123841], [0.0751136, 0.123841, 0.0751136]])
    Gaussian_img = cv2.filter2D(img_gray2, -1, kernel)
    cv2.imshow('filter2D', Gaussian_img)
    cv2.imwrite('filter2D_1.jpg', Gaussian_img)
    cv2.waitKey(1)
    res = cv2.matchTemplate(Gaussian_img, template, 0)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = min_loc
    img2 = img.copy()
    cv2.rectangle(img2, min_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.rectangle(Gaussian_img, min_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.imwrite('filter2D_2.jpg', Gaussian_img)
    cv2.imshow('filter2D_match', img2)
    cv2.imwrite('filter2D_3.jpg', img2)
    cv2.waitKey(1)


    # 使用GaussianBlur函数滤波处理
    img_gray3 = img_gray.copy()
    kernel_size = (3, 3)
    Gaussian_img = cv2.GaussianBlur(img_gray3, kernel_size, sigma)
    cv2.imshow('GaussianBlur', Gaussian_img)
    cv2.imwrite('GaussianBlur_1.jpg', Gaussian_img)
    cv2.waitKey(1)
    res = cv2.matchTemplate(Gaussian_img, template, 0)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    x, y = min_loc
    img3 = img.copy()
    cv2.rectangle(img3, min_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.rectangle(Gaussian_img, min_loc, (x + template.shape[0], y + template.shape[1]), (0, 255, 0), 2)
    cv2.imwrite('GaussianBlur_2.jpg', Gaussian_img)
    cv2.imshow('GaussianBlur_match', img3)
    cv2.imwrite('GaussianBlur_3.jpg', img3)
    cv2.waitKey(0)
