# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd


def get_dis3_circle():
    """
    获取具有趋势的三级地区
    :return: 在三级地区中具有趋势性的地区
    """
    train_district3 = pd.read_csv('../pro_data/train_district3.csv', index_col=0)
    l = []
    for i in train_district3.index:
        s = train_district3.loc[i]
        s.reset_index(drop=True, inplace=True)
        largest = s.nlargest(4).index
        if np.abs(largest[0] - largest[1]) == 12:
            l.append(i)
            continue
        if np.abs(largest[0] - largest[1]) == 1 and np.abs(largest[2] - largest[3]) == 1 \
           and np.abs(largest[0]+largest[1] - largest[2] - largest[3]) == 24:
            l.append(i)
    return l
