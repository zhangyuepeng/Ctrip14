# -*- coding: UTF-8 -*-
import numpy as np


def predict_5_12(s, start, voters):
    """
    对历史销量数据在5到12个月之间的出行产品进行预测
    :param s: 历史销量
    :param start: 开始具有销量的时间标记
    :param voters: 投票数
    :return: 预测的14个月销量
    """
    a = 0.6
    b = 0.4
    c = 0.1
    length = len(s)
    result = [0]*14
    month_count = length - start
    result[0] = (0.4 * s[-1] + 0.3 * s[-2] + 0.3 * s[-3])
    # 由于其销量月份比较少难以有效学习销量，而早期销量又不够稳定，所以算法我们比较多的依赖的后期销量
    # 以及voters修正处理
    if month_count == 11:
        for i in range(11, 8, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.35 * mean_ + 0.35 * result[0] + 0.3 * s[-1]
        for j in range(1, 4):
            if s[-12+j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5*mean_ + 0.5*result[j-1]
        for k in range(j+1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 10:
        for i in range(10, 7, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.3 * mean_ + 0.3 * result[0] + 0.4 * s[-1]
        result[1] = 0.35 * mean_ + 0.35 * result[0] + 0.3 * s[-1]
        for j in range(2, 5):
            if s[-12 + j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j-1]
        for k in range(j+1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 9:
        for i in range(9, 6, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.25 * mean_ + 0.25 * result[0] + 0.5 * s[-1]
        result[1] = 0.3 * mean_ + 0.3 * result[0] + 0.4 * s[-1]
        result[2] = 0.35 * mean_ + 0.35 * result[1] + 0.3 * s[-1]
        for j in range(3, 6):
            if s[-12 + j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j - 1]
        for k in range(j + 1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 8:
        for i in range(8, 5, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.25 * mean_ + 0.25 * result[0] + 0.5 * s[-1]
        result[1] = 0.3 * mean_ + 0.3 * result[0] + 0.4 * s[-1]
        result[2] = 0.35 * mean_ + 0.35 * result[1] + 0.3 * s[-1]
        result[3] = 0.4 * mean_ + 0.4 * result[2] + 0.2 * s[-1]
        for j in range(4, 7):
            if s[-12 + j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j - 1]
        for k in range(j + 1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 7:
        for i in range(7, 4, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.2 * mean_ + 0.2 * result[0] + 0.6 * s[-1]
        result[1] = 0.25 * mean_ + 0.25 * result[0] + 0.5 * s[-1]
        result[2] = 0.3 * mean_ + 0.3 * result[1] + 0.4 * s[-1]
        result[3] = 0.35 * mean_ + 0.35 * result[2] + 0.3 * s[-1]
        result[4] = 0.4 * mean_ + 0.4 * result[3] + 0.2 * s[-1]
        for j in range(5, 8):
            if s[-12 + j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j - 1]
        for k in range(j + 1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 6:
        for i in range(6, 3, -1):
            if s[-i] > c * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.2 * mean_ + 0.2 * result[0] + 0.6 * s[-1]
        result[1] = 0.25 * mean_ + 0.25 * result[0] + 0.5 * s[-1]
        result[2] = 0.3 * mean_ + 0.3 * result[1] + 0.4 * s[-1]
        result[3] = 0.35 * mean_ + 0.35 * result[2] + 0.3 * s[-1]
        result[4] = 0.4 * mean_ + 0.4 * result[3] + 0.2 * s[-1]
        result[5] = 0.45 * mean_ + 0.45 * result[4] + 0.1 * s[-1]
        for j in range(6, 9):
            if s[-12 + j] > c * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j - 1]
        for k in range(j + 1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    elif month_count == 5:
        for i in range(5, 2, -1):
            if s[-i] > 0.07 * voters and voters > 0:
                break
        mean_ = s[-i:].mean()
        result[0] = 0.2 * mean_ + 0.2 * result[0] + 0.6 * s[-1]
        result[1] = 0.25 * mean_ + 0.25 * result[0] + 0.5 * s[-1]
        result[2] = 0.3 * mean_ + 0.3 * result[1] + 0.4 * s[-1]
        result[3] = 0.35 * mean_ + 0.35 * result[2] + 0.3 * s[-1]
        result[4] = 0.4 * mean_ + 0.4 * result[3] + 0.2 * s[-1]
        result[5] = 0.45 * mean_ + 0.45 * result[4] + 0.1 * s[-1]
        result[6] = 0.45 * mean_ + 0.45 * result[5] + 0.1 * s[-1]
        for j in range(7, 10):
            if s[-12 + j] > 0.1 * voters and voters > 0:
                result[j] = 0.5 * a * s[-12 + j] + b * mean_ + 0.5 * a * result[j - 1]
                break
            else:
                result[j] = 0.5 * mean_ + 0.5 * result[j - 1]
        for k in range(j + 1, 12):
            result[k] = a * s[-12 + k] + b * mean_
    result[12] = result[0]
    result[13] = result[1]
    result = np.array(result)
    # 利用voters特征对预测结果进行修正
    if result.max() < 0.1 * voters:
        result = 0.5 * result + 0.5 * 0.1 * voters
        result[0] = 0.75 * s[-1] + 0.25 * result[0]
        result[1] = 0.5 * s[-1] + 0.5 * result[1]
        result[2] = 0.25 * s[-1] + 0.75 * result[2]
    elif result.min() > 0.2 * voters and voters > 10:
        ratio = result.mean() / voters + 0.2
        if ratio < 0.5:
            result = 0.5 * result + 0.5 * 0.2 * voters
        elif ratio > 0.7:
            result = 0.3 * result + 0.7 * 0.2 * voters
        else:
            result = (1 - ratio) * result + ratio * 0.2 * voters
        result[0] = 0.75 * s[-1] + 0.25 * result[0]
        result[1] = 0.5 * s[-1] + 0.5 * result[1]
        result[2] = 0.25 * s[-1] + 0.75 * result[2]
    else:
        result[0] = 0.5 * s[-1] + 0.5 * result[0]
        result[1] = 0.25 * s[-1] + 0.75 * result[1]
    return result
