# -*- coding: UTF-8 -*-


def predict_1_5(s, start, voters):
    """
    对历史销量数据在1到5个月之间的出行产品进行预测
    :param s: 历史销量
    :param start: 开始具有销量的时间标记
    :param voters: 投票数
    :return: 预测的14个月销量
    """
    length = len(s)
    month_count = length - start
    c = 0.16
    result = [0] * 14
    # 这个类别具有的销量时间十分短，从已有数据的统计判断，开始销量往往会比较小所以算法大量利用了voters来修正销量预测。
    if month_count == 4:
        sale = 0.4*s[-1] + 0.3*s[-2] + 0.2*s[-3] + 0.1*s[-4]
        if voters > 0:
            for i in range(4, 0, -1):
                if s[-i] < 0.03*voters:
                    sale += 0.1*s[-i]
                else:
                    break
            sale = 0.5*sale + 0.5 * c*voters
        result = [sale] * 14
        result[0] = 0.5 * s[-1] + 0.5 * result[0]
        result[1] = 0.25 * s[-1] + 0.75 * result[1]
    elif month_count == 3:
        sale = 0.5*s[-1] + 0.3*s[-2] + 0.2*s[-3]
        if voters > 0:
            for i in range(3, 0, -1):
                if s[-i] < 0.03*voters:
                    sale += 0.15*s[-i]
                else:
                    break
            sale = 0.5*sale + 0.5 * c*voters
        result = [sale] * 14
        result[0] = 0.5 * s[-1] + 0.5 * result[0]
        result[1] = 0.25 * s[-1] + 0.75 * result[1]
    else:
        if month_count == 2:
            sale = 0.7*s[-1] + 0.3*s[-2]
            if voters > 0:
                for i in range(2, 0, -1):
                    if s[-i] < 0.03 * voters:
                        sale += 0.2 * s[-i]
                    else:
                        break
                sale = 0.5 * sale + 0.5 * c*voters
            result = [sale] * 14
            result[0] = 0.5 * s[-1] + 0.5 * result[0]
            result[1] = 0.25 * s[-1] + 0.75 * result[1]
        else:
            c = 0.135
            ratio = s[-1] / voters
            if 2 > ratio > 0.135:
                result[0] = result[1] = result[2] = result[3] = s[-1]
            elif ratio > 2:
                result[0] = result[1] = result[2] = result[3] = 0.2 * voters
            elif ratio > 0.04:
                result[0] = s[-1] + voters * (0.135 - ratio) / 4
                result[1] = result[0] + voters * (0.135 - ratio) / 4
                result[2] = result[1] + voters * (0.135 - ratio) / 4
                result[3] = result[2] + voters * (0.135 - ratio) / 4
            else:
                result[0] = 0.04 * voters
                result[1] = 0.06 * voters
                result[2] = 0.09 * voters
                result[3] = 0.12 * voters
            for i in range(4, 14):
                result[i] = c * voters
                if s[-1] > result[i]:
                    result[i] = (s[-1] + result[i]) / 2
    return result
