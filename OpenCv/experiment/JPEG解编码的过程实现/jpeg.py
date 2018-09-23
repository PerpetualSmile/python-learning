import cv2
import numpy as np


lighttable = np.array([[16,11,10,16,24,40,51,61],
    [12,12,14,19,26,58,60,55] ,
    [14,13,16,24,40,57,69,56 ] ,
    [14,17,22,29,51,87,80,62 ],
    [18,22,37,56,68,109,103,77],
    [24,35,55,64,81,104,113,92] ,
    [49,64,78,87,103,121,120,101],
    [72,92,95,98,112,100,103,99]], dtype='float64')
colortable = np.array([
    [17,18,24,47,99,99,99,99] ,
    [18,21,26,66,99,99,99,99] ,
    [24,26,56,99,99,99,99,99],
    [47,66,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99],
    [99,99,99,99,99,99,99,99]], dtype='float64')


def encode_jpeg(img):
    img = np.float64(img)


    # DCT变换
    for i in range(img.shape[2]):
        img[:, :, i] = cv2.dct(img[:, :, i] - 128.0)
    img[:, :, 0] = np.int32(img[:, :, 0] / lighttable)
    img[:, :, 1] = np.int32(img[:, :, 1] / colortable)
    img[:, :, 2] = np.int32(img[:, :, 2] / colortable)
    # Z字形扫描
    code_list = []
    for channel in range(channels):
        code = []
        i = 0
        j = 0
        last_i = 0
        last_j = 0
        while True:
            code.append(img[i, j, channel])
            # 左上顶点
            if i == 0 and j == 0:
                last_i = i
                last_j = j
                j += 1
                continue
            # 右下顶点结束
            if i == img.shape[0] - 1 and j == img.shape[1] - 1:
                break
            # 上边界
            if i == 0:
                # 往左下
                if last_i == 0:
                    last_i = i
                    last_j = j
                    i += 1
                    j -= 1
                # 横向
                else:
                    last_i = i
                    last_j = j
                    j += 1
                continue
            # 下边界
            if i == img.shape[0] - 1:
                # 往右上
                if last_i == i:
                    last_i = i
                    last_j = j
                    j += 1
                    i -= 1
                # 横向
                else:
                    last_i = i
                    last_j = j
                    j += 1
                continue
            # 左边界
            if j == 0:
                # 往右上
                if last_j == 0:
                    last_i = i
                    last_j = j
                    j += 1
                    i -= 1
                # 纵向
                else:
                    last_i = i
                    last_j = j
                    i += 1
                continue
            # 右边界
            if j == img.shape[1] - 1:
                # 往左下
                if last_j == j:
                    last_i = i
                    last_j = j
                    i += 1
                    j -= 1
                # 纵向
                else:
                    last_i = i
                    last_j = j
                    i += 1
                continue

            # 左下
            if last_i == i - 1 and last_j == j + 1:
                last_i = i
                last_j = j
                i += 1
                j -= 1
                continue
            # 右上
            if last_i == i + 1 and last_j == j - 1:
                last_i = i
                last_j = j
                i -= 1
                j += 1
        code_list.append(code)
    # 游程编码
    result = []
    for code in code_list:
        temp = []
        last = code[0]
        count = 1
        for i in range(1, len(code)):
            if code[i] == last:
                count += 1
            else:
                temp.append(count)
                temp.append(last)
                count = 1
                last = code[i]
        temp.append(count)
        temp.append(last)
        result.append(temp)
    return result

def decode_jpeg(code_list):
    img = np.zeros((8, 8, len(code_list)))
    z = []
    channel = 0
    # 解游程编码
    for code in code_list:
        temp = []
        for i in range(0, len(code), 2):
            for j in range(code[i]):
                temp.append(code[i + 1])
        z.append(temp)

    # 还原Z字形扫描
    for channel in range(len(code_list)):
        count = 0
        i = 0
        j = 0
        last_i = 0
        last_j = 0
        while True:
            img[i, j, channel] = z[channel][count]
            count += 1
            # 左上顶点
            if i == 0 and j == 0:
                last_i = i
                last_j = j
                j += 1
                continue
            # 右下顶点结束
            if i == img.shape[0] - 1 and j == img.shape[1] - 1:
                break
            # 上边界
            if i == 0:
                # 往左下
                if last_i == 0:
                    last_i = i
                    last_j = j
                    i += 1
                    j -= 1
                # 横向
                else:
                    last_i = i
                    last_j = j
                    j += 1
                continue
            # 下边界
            if i == img.shape[0] - 1:
                # 往右上
                if last_i == i:
                    last_i = i
                    last_j = j
                    j += 1
                    i -= 1
                # 横向
                else:
                    last_i = i
                    last_j = j
                    j += 1
                continue
            # 左边界
            if j == 0:
                # 往右上
                if last_j == 0:
                    last_i = i
                    last_j = j
                    j += 1
                    i -= 1
                # 纵向
                else:
                    last_i = i
                    last_j = j
                    i += 1
                continue
            # 右边界
            if j == img.shape[1] - 1:
                # 往左下
                if last_j == j:
                    last_i = i
                    last_j = j
                    i += 1
                    j -= 1
                # 纵向
                else:
                    last_i = i
                    last_j = j
                    i += 1
                continue

            # 左下
            if last_i == i - 1 and last_j == j + 1:
                last_i = i
                last_j = j
                i += 1
                j -= 1
                continue
            # 右上
            if last_i == i + 1 and last_j == j - 1:
                last_i = i
                last_j = j
                i -= 1
                j += 1

    # 逆DCT变换
    img[:, :, 0] = np.int32(img[:, :, 0] * lighttable)
    img[:, :, 1] = np.int32(img[:, :, 1] * colortable)
    img[:, :, 2] = np.int32(img[:, :, 2] * colortable)
    img = np.float64(img)
    for i in range(img.shape[2]):
        img[:, :, i] = np.uint8(cv2.idct(img[:, :, i]) + 128)
    return img

if __name__ == '__main__':
    img = cv2.imread('lena.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    raw_img = img.copy()
    # 图像分块
    height, weight, channels = img.shape
    img = np.vstack((img, np.zeros((height % 8, weight, channels), dtype='uint8')))
    img = np.hstack((img, np.zeros((img.shape[0], weight % 8, channels), dtype='uint8')))

    # 图像编码
    result_img = np.zeros(img.shape)
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            # jpeg编码，返回游程编码的结果
            result = encode_jpeg(img[i:i + 8, j:j + 8])
            # jpeg解码，返回解码后的图像块, 并进行图像拼接
            result_img[i:i + 8, j:j + 8] = decode_jpeg(result)

    img = cv2.cvtColor(np.uint8(result_img), cv2.COLOR_YCrCb2BGR)
    cv2.imwrite('lena_result.png', img)