# -*- coding: UTF-8 -*-

import pandas as pd

'''
对不同的三级地区，统计其月销量。
'''
product_info = pd.read_csv('../data/product_info.txt')
product_info = product_info[['product_id', 'district_id3']]
product_quantity = pd.read_csv('../data/product_quantity.txt')
product_quantity.sort_values(['product_id', 'product_date'], inplace=True)
product_quantity['product_month'] = product_quantity['product_date'].apply(lambda x: x[:7])
pq = product_quantity.merge(product_info, how='left', on='product_id')
train_district3 = pq.groupby(['district_id3', 'product_month']).sum()['ciiquantity'].unstack()
train_district3 = train_district3.fillna(0)
train_district3.to_csv('../pro_data/train_district3.csv')
