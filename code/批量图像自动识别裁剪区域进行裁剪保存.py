# -*- coding: utf-8 -*-
import cv2
import numpy as np

import copy
import cv2 as cv
import os


def read_path(file_pathname):
    # 遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        src = cv.imread(file_pathname + '/' + filename)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        width = gray.shape[0]  # 图片行
        height = gray.shape[1]  # 图片列
        green_max = np.zeros(2)  # 一行两列0
        green_min = np.zeros(2)
        # print(green_max)

        a_list = []
        for i in range(width):
            for j in range(height):
                gray_value = gray[i, j]
                if gray_value > 20:
                    a = np.array([i, j])
                    a_list.append(a)  # 所有黑色区域坐标点
        # print(a_list[1])
        # print(a_list)
        # 最大坐标
        green_max = a_list[1]
        for g, k in enumerate(a_list):

            if k[0] > green_max[0]:
                green_max[0] = int(k[0])
            else:
                green_max[0] = int(green_max[0])

                if k[1] > green_max[1]:
                    green_max[1] = int(k[1])
                else:
                    green_max[1] = int(green_max[1])
                # print(green_max)

            # 最小坐标
            green_min = a_list[0]
            # print(green_min)
            for h, z in enumerate(a_list):
                # print(green_min)
                if z[0] < green_min[0]:
                    green_min[0] = z[0]
                else:
                    green_min[0] = green_min[0]

                    if z[1] < green_min[1]:
                        green_min[1] = z[1]
                    else:
                        green_min[1] = green_min[1]

            dst = src[int(green_min[0] - 80):int(green_max[0] + 60), int(green_min[1] - 60):int(green_max[1] + 60)]
            # cv.imshow('gray', dst)
            cv.imwrite('D:/Anaconda3/test7' + "/" + filename, dst)


read_path("09")