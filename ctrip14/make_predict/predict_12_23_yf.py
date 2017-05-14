# -*- coding: UTF-8 -*-

import numpy as np


def predict_12_23_yf(s, flag):
    """
    对历史销量数据在12到23个月之间的出行产品进行预测
    :param s: 历史销量
    :param flag: 所在的三级地区是否具有已统计的趋势
    :return: 预测的14个月销量
    """
    mean_12 = s[-12:].mean()
    mean_8 = s[-8:].mean()
    result = [0] * 14
    four_mean = s[-4:].mean()
    eight_mean = s[-8:-4].mean()
    tw_mean = s[-12:-8].mean()

    # 增长趋势：连续3个
    if four_mean > eight_mean > tw_mean:
        four_mean = s[-4:].mean()
        eight_mean = s[-8:-4].mean()
        tw_mean = s[-12:-8].mean()
        ts = np.array([1, 1, 1, 1, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.6, 0.6])
        tred = ((four_mean - eight_mean) / (eight_mean + 1) + (eight_mean - tw_mean) / (tw_mean + 1)) / 2
        if tred > 0.25:
            tred = 0.25
            ts = (tred * ts + 1) * (tred * ts + 1) * (tred * ts + 1)
        result[0] = (0.3 * s[-12] * ts[0] + 0.1 * mean_12 + 0.2 * four_mean + 0.4 * eight_mean+ s[-1]) / 2
        result[1] = (0.3 * s[-11] * ts[1] + 0.1 * mean_12 + 0.2 * four_mean + 0.4 * eight_mean + result[0]) / 2
        result[2:12] = 0.3 * s[-10:] * ts[2:] + 0.1 * mean_12 + 0.2 * four_mean + 0.4 * eight_mean
        result[12] = result[0]
        result[13] = result[1]
        return result
    else:
        if flag:
            result[0] = (0.45 * s[-12] + 0.1 * mean_12 + 0.25 * four_mean + 0.2 * mean_8 + s[-1]) / 2
            result[1] = (0.45 * s[-11] + 0.1 * mean_12 + 0.25 * four_mean + 0.2 * mean_8 + result[0]) / 2
            result[2:12] = 0.45 * s[-10:] + 0.1 * mean_12 + 0.25 * four_mean + 0.2 * mean_8
            result[12] = result[0]
            result[13] = result[1]
            return result
        result[0] = (0.15 * s[-12] + 0.2 * mean_12 + 0.4 * four_mean + 0.25 * mean_8 + s[-1]) / 2
        result[1] = (0.15 * s[-11] + 0.2 * mean_12 + 0.4 * four_mean + 0.25 * mean_8 + result[0]) / 2
        result[2:12] = 0.15 * s[-10:] + 0.2 * mean_12 + 0.4 * four_mean + 0.25 * mean_8
        result[12] = result[0]
        result[13] = result[1]
    return result
