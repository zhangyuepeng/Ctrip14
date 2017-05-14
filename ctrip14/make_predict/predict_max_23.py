# -*- coding: UTF-8 -*-

import numpy as np


def predict_max_23(s):
    """
    对从开始月份就有销量的出行产品进行预测
    :param s:历史销量
    :return: 预测的14个月销量
    """
    first11 = np.array(s[:11])
    last11 = np.array(s[-11:])
    mean_10 = (s[-12:].sum() - s[-12:].min() - s[-12:].max()) / 10
    mean_4 = (s[-6:].sum() - s[-6:].min() - s[-6:].max()) / 4
    mean_4_1 = (s[-4:].sum()) / 4
    result = 0.25 * s[-12:] + 0.75 * mean_10
    result = np.array(result)
    # 利用前11个月和后11个月的相关系数来刻画一定的周期性，相关系数越大认为周期性越高，
    if np.median(first11) > 3 and np.median(last11) > 3:
        cor = np.corrcoef(first11, last11)[0, 1]
        if cor > 0:
            first11 = first11 / first11.mean()
            last11 = last11 / last11.mean()
            ratio = 0.6 * last11 + 0.4 * first11
            cc = 0.5
            result[0] = 0.15 * s[11] + cc * cor * s[11] + 0.2*(1-cor)*mean_4 + (1-0.15-cc*cor-0.2*(1-cor))*mean_10
            result[1:] = 0.15*s[-11:] + cc*cor*ratio*mean_10 + 0.2*(1-cor)*mean_4 + (1-0.15-cc*cor-0.2*(1-cor))*mean_10
        else:
            cc = 0.5
            result[0:] = 0.15 * s[-12:] + 0.2 * mean_4 + cc*(-cor)*mean_4 + (1-0.15-0.2+cc*cor)*mean_10
        # 加进增长的趋势项。
        # 对数据进行两次移动平均，利用其刻画趋势，如果其后期增长时间较长并且基本方式求出的均值结果较小
        # 则认为其有增长趋势
        # 然后利用斜率的中位数来对增长趋势进行刻画
        s_mean_1 = s.rolling(5, min_periods=1, center=True).mean()
        s_mean_2 = s_mean_1.rolling(5, min_periods=1, center=True).mean()
        ratio = 1
        if s_mean_2[-1] >= s_mean_2[-2]:
            count = 1
            for j in range(2, 10):
                if s_mean_2[-j] >= s_mean_2[-j-1]:
                    count += 1
                else:
                    break
            if count >= 8 and result.mean() < 0.8 * mean_4_1:
                ratio = np.median([s_mean_2[-1]/s_mean_2[-2], s_mean_2[-2]/s_mean_2[-3], s_mean_2[-3]/s_mean_2[-4],
                                   s_mean_2[-4]/s_mean_2[-5], s_mean_2[-5]/s_mean_2[-6], s_mean_2[-6]/s_mean_2[-7],
                                  s_mean_2[-7]/s_mean_2[-8], s_mean_2[-8]/s_mean_2[-9], s_mean_2[-9]/s_mean_2[-10],
                                  s_mean_2[-10]/s_mean_2[-11]])
                ratio = np.power(ratio, 4)
                if ratio < 1.15:
                    result = result + mean_10 * (ratio - 1)
                else:
                    ratio = 1.15 + (ratio - 1.15) / np.sqrt(ratio)
                    if ratio < 1.25:
                        result = result + mean_10 * (ratio - 1)
                    else:
                        result = result + mean_10 * 0.25
            else:
                count = 1
                for j in range(2, 13):
                    if s_mean_2[-j] >= s_mean_2[-j - 1]:
                        count += 1
                if count >= 10 and result.mean() < 0.8 * mean_4_1:
                    ratio = np.median(
                        [s_mean_2[-1] / s_mean_2[-2], s_mean_2[-2] / s_mean_2[-3], s_mean_2[-3] / s_mean_2[-4],
                         s_mean_2[-4] / s_mean_2[-5], s_mean_2[-5] / s_mean_2[-6], s_mean_2[-6] / s_mean_2[-7],
                         s_mean_2[-7] / s_mean_2[-8], s_mean_2[-8] / s_mean_2[-9], s_mean_2[-9] / s_mean_2[-10],
                         s_mean_2[-10] / s_mean_2[-11]])
                    ratio = np.power(ratio, 4)
                    if ratio < 1.15:
                        result = result + mean_10 * (ratio - 1)
                    else:
                        ratio = 1.15 + (ratio - 1.15) / np.sqrt(ratio)
                        if ratio < 1.25:
                            result = result + mean_10 * (ratio - 1)
                        else:
                            result = result + mean_10 * 0.25
        result = result.tolist()
        # 对早期两个月的预测加入平滑处理，并对最后两个月增大趋势或加入平滑处理
        if ratio > 1.8:
            result.append(result[0] * 1.8)
            result.append(result[1] * 1.8)
        elif ratio > 1:
            result.append(result[0] * ratio)
            result.append(result[1] * ratio)
        else:
            result.append(0.6 * result[0] + 0.4 * result[11])
            result.append(0.6 * result[1] + 0.4 * result[11])
        if cor < 0:
            result[0] = 0.5 * s[-1] + 0.5 * result[0]
            result[1] = 0.25 * s[-1] + 0.75 * result[1]
        else:
            result[0] = 0.5 * (1-cor) * s[-1] + (0.5 + 0.5 * cor)*result[0]
            result[1] = 0.25 * (1-cor) * s[-1] + (0.75 + 0.25*cor)*result[1]
    else:
        result = result.tolist()
        result.append(result[0])
        result.append(result[1])
        result[0] = 0.5 * s[-1] + 0.5 * result[0]
        result[1] = 0.25 * s[-1] + 0.75 * result[1]
    return result
