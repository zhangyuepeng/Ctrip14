# -*- coding: UTF-8 -*-

import datetime as dt
import numpy as np


def predict_no(voters, startdate, cooperatedate, trend):
    """
    此算法在预测没有历史销量数据时，我们默认从合作时间和开始时间（我们会对时间的合理性进行判断）的最小值开始处理产生销量。
    同时利用地区的趋势和voters来共同预测销量。
    :param voters: 投票数
    :param startdate: 开始时间（字符串类型）
    :param cooperatedate: 合作时间（字符串类型）
    :param trend: 按区域统计的趋势
    :return: 预测的14个月销量
    """
    std = dt.datetime(2015, 11, 30)
    if voters <= 0:
        result = [0] * 14
    else:
        if startdate != '-1' and startdate != '1753-01-01' and cooperatedate != '-1' and cooperatedate != '1753-01-01':
            start_date = dt.datetime.strptime(startdate, "%Y-%m-%d")
            start_delta_days = (std - start_date).days
            cooperate_date = dt.datetime.strptime(cooperatedate, "%Y-%m-%d")
            cooperate_delta_days = (std - cooperate_date).days
            if cooperate_delta_days <= 0 and start_delta_days <= 0:
                if cooperate_delta_days - start_delta_days < 32.1:
                    start = get_start(startdate[:7])
                    result = give_value_startdate(voters, start, trend)
                else:
                    start = get_start(cooperatedate[:7])
                    start_day = float(cooperatedate[-2:])
                    result = give_value_cooperatedate(voters, start, start_day, trend)
            elif 0 < cooperate_delta_days < 48 or 0 < start_delta_days < 48:
                result = give_value_startdate(voters, 0, trend)
            else:
                if start_delta_days < 0:
                    start = get_start(startdate[:7])
                    result = give_value_startdate(voters, start, trend)
                elif cooperate_delta_days < 0:
                    start = get_start(cooperatedate[:7])
                    start_day = float(cooperatedate[-2:])
                    result = give_value_cooperatedate(voters, start, start_day, trend)
                else:
                    result = give_value_startdate(voters, 0, trend)
        elif startdate != '-1' and startdate != '1753-01-01':
            start_date = dt.datetime.strptime(startdate, "%Y-%m-%d")
            start_delta_days = (std - start_date).days
            if start_delta_days < 0:
                start = get_start(startdate[:7])
                result = give_value_startdate(voters, start, trend)
            else:
                result = give_value_startdate(voters, 0)
        elif cooperatedate != '-1' and cooperatedate != '1753-01-01':
            cooperate_date = dt.datetime.strptime(cooperatedate, "%Y-%m-%d")
            cooperate_delta_days = (std - cooperate_date).days
            if cooperate_delta_days < 0:
                start = get_start(cooperatedate[:7])
                start_day = float(cooperatedate[-2:])
                result = give_value_cooperatedate(voters, start, start_day, trend)
            else:
                result = give_value_startdate(voters, 0, trend)
        else:
            result = give_value_startdate(voters, 0, trend)
    result = np.array(result)
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


def give_value_cooperatedate(voters, start, start_day, trend):
    result = give_value_startdate(voters, start, trend)
    if start < 13:
        ratio = 1 - start_day / 31
        result[start] = ratio * result[start]
        add_in = ((1 - ratio) * result[start]) / (13 - start)
        for i in range(start + 1, 14):
            result[i] += add_in
    return result


def give_value_startdate(voters, start, trend):
    ave = 3 * voters / (14 - start)
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
