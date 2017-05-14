# -*- coding: UTF-8 -*-


def predict_no_yf(voters, startdate, cooperatedate, trend):
    """
    此算法利用合作时间来预测没有历史销量数据的未来14个月的销量
    :param voters: 投票数
    :param startdate: 开始时间（字符串类型）
    :param cooperatedate: 合作时间（字符串类型）
    :param trend: 按区域统计的趋势
    :return: 预测的14个月销量
    """
    if voters <= 0:
        return [0] * 14
    else:
        if cooperatedate != '-1' and cooperatedate != '1753-01-01':
            start = get_start(cooperatedate[0:7])
            if start != -1:
                return give_value_by_trend(voters, start, trend)
            else:
                if startdate != '-1' and startdate != '1753-01-01':
                    start = get_start(startdate[0:7])
                    if start != -1:
                        return give_value_by_trend(voters, start, trend)
                    else:
                        return [0] * 14
                else:
                    return [0] * 14


def give_value_by_trend(voters, start, trend):
    ave = 3 * voters/(14 - start)
    result = [0] * 14
    if start > -1:
        if trend is None:
            for i in range(0, 14):
                if i < start:
                    result[i] = 0
                elif i == start:
                    result[i] = 0.3 * ave
                elif i == start + 1:
                    result[i] = 0.5 * ave
                elif i == start + 2:
                    result[i] = 0.7 * ave
                else:
                    result[i] = ave
            return result
        else:
            for i in range(0, 14):
                if i < start:
                    result[i] = 0
                elif i == start:
                    result[i] = 0.3 * ave
                elif i == start + 1:
                    result[i] = 0.5 * ave
                elif i == start + 2:
                    result[i] = 0.7 * ave
                else:
                    result[i] = ave * trend[i]
            return result
    else:
        return result


def get_start(strdate):
    if strdate == '2015-12':
        return 0
    elif strdate == '2017-01':
        return 13
    elif strdate[:4] == '2016':
        return int(strdate[-2:])
    else:
        return -1
