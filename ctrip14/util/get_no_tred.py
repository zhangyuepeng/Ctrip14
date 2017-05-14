# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np


def get_no_trend():
    """
    获得三级地区的趋势
    :return: 在三级地区的趋势(各月销量占平均值的比率)
    """
    dic = {}
    train_district3 = pd.read_csv('../pro_data/train_district3.csv', index_col=0)
    for i in train_district3.index:
        s = train_district3.loc[i]
        flag = len(s)
        for j in range(len(s)):
            if s[j] > 0:
                flag = j
                break
        if flag > 10:
            dic[i] = None
        else:
            tred = s[-12:] / s[-12:].mean()
            tred = tred.tolist()
            tred.append(tred[0])
            tred.append(tred[1])
            dic[i] = np.sqrt(tred)
    return dic
