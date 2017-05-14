# -*- coding: UTF-8 -*-

import pandas as pd

'''
对每个出行产品，统计其月销量。
'''
product_quantity = pd.read_csv('../data/product_quantity.txt')
product_quantity.sort_values(['product_id', 'product_date'], inplace=True)
product_quantity['product_month'] = product_quantity['product_date'].apply(lambda x: x[:7])
train_month = product_quantity.groupby(['product_id', 'product_month']).sum()['ciiquantity'].unstack()
train_month = train_month.fillna(0)
train_month.to_csv('../pro_data/train_month.csv')

