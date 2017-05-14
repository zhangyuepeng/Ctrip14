# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np


'''
提取具有明显周期性的出行产品的月销量
'''
product_info = pd.read_csv('../data/product_info.txt', index_col=0)
product_quantity = pd.read_csv('../data/product_quantity.txt')
product_quantity = product_quantity[product_quantity.ciiquantity > 0]
product_quantity.sort_values(['ciiquantity'], ascending=False, inplace=True)
l = []
for i in product_info.index:
    d = product_quantity[product_quantity['product_id'] == i]
    d.reset_index(inplace=True)
    s = d.shape[0]/100
    d = d[d.index > (s-1)]
    l.append(d)
product_quantity = pd.concat(l)
product_quantity['product_month'] = product_quantity['product_date'].apply(lambda x: x[:7])
train_month = product_quantity.groupby(['product_id', 'product_month']).sum()['ciiquantity'].unstack()
train_month.fillna(0, inplace=True)
train_month.to_csv('../pro_data/pro_train_month.csv')

train_circle = []
train_month = pd.read_csv('../pro_data/pro_train_month.csv',index_col=0)
for i in train_month.index:
    s = train_month.loc[i]
    s.reset_index(drop=True, inplace=True)
    largest = s.nlargest(2).index
    if np.abs(largest[0] - largest[1]) == 12:
        if i not in train_circle:
            train_circle.append(i)
            continue
    largest = s.nlargest(4).index
    if np.abs(largest[0] - largest[1]) == 1 and np.abs(largest[2] - largest[3]) == 1 \
       and np.abs(largest[0]+largest[1] - largest[2] - largest[3]) == 24:
        if i not in train_circle:
            train_circle.append(i)
            continue

for i in train_month.index:
    if i not in train_circle:
        train_month.drop(i, inplace=True)

train_month.to_csv('../pro_data/circle.csv')



