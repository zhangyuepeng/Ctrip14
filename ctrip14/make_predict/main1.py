# -*- coding: UTF-8 -*-

from predict_1_5 import *
from predict_5_12 import *
from predict_no import *
from predict_12_23_yf import *
from predict_max_23 import *
from predict_circle import *
from predict_no_yf import *
from util.get_dis3_circle import *
from util.pro_is_flag import *
from util.get_no_tred import *


circle = pd.read_csv('../pro_data/circle.csv', index_col=0)
train_district3 = pd.read_csv('../pro_data/train_district3.csv', index_col=0)
product_info = pd.read_csv('../data/product_info.txt', index_col=0)
train_month = pd.read_csv('../pro_data/train_month.csv', index_col=0)
predict = pd.read_csv('../data/prediction_lilei.txt', index_col=[0, 1])
predict['ciiquantity_month'] = 0
predict = predict.unstack()
length = len(train_month.columns)
l = get_dis3_circle()
dic = get_no_trend()

for i in predict.index:
    if i in train_month.index:
        s = train_month.loc[i]
        flag = length  # flag代表开始具有销量时的月份下标
        for j in range(0, length):
            if s[j] > 0:
                flag = j
                break
        if i in circle.index:  # 如果其具有强烈的周期性，则进行周期性预测
            s = circle.loc[i]
            predict.loc[i] = predict_cricle(s)
            continue
        if length - flag == 23:  # 对历史销量都存在的出行产品进行预测
            r1 = predict_max_23(s)
            predict.loc[i] = np.array(r1)
        elif length - flag >= 12:  # 对历史销量在12到23个月之间的出行产品进行预测
            d = product_info.at[i, 'district_id3']
            flag1 = isflag(d, l)
            predict.loc[i] = predict_12_23_yf(s, flag1)
        elif length - flag > 4:  # 对历史销量在5到12个月之间的出行产品进行预测
            predict.loc[i] = predict_5_12(s, flag, product_info.at[i, 'voters'])
        elif length - flag > 0:  # 对历史销量在1到5个月之间的出行产品进行预测
            predict.loc[i] = predict_1_5(s, flag, product_info.at[i, 'voters'])
        else:  # 对只有预订单而没有历史销量的出行产品进行预测
            d = product_info.at[i, 'district_id3']
            trend = None
            if d in dic:
                trend = dic[d]
            predict.loc[i] = np.array(give_value_startdate(product_info.at[i, 'voters'], 0, trend))
    else:  # 对没有订单数据的出行产品进行预测
        d = product_info.at[i, 'district_id3']
        trend = None
        if d in dic:
            trend = dic[d]
        r1 = predict_no(product_info.at[i, 'voters'],
                        product_info.at[i, 'startdate'], product_info.at[i, 'cooperatedate'], trend)
        r2 = predict_no_yf(product_info.at[i, 'voters'],
                           product_info.at[i, 'startdate'], product_info.at[i, 'cooperatedate'], trend)
        predict.loc[i] = (0.5 * np.array(r1) + 0.5 * np.array(r2))
predict.columns = ['2015-12-01', '2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01',
                   '2016-07-01', '2016-08-01', '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01', '2017-01-01']
predict = predict.unstack()
predict.name = 'ciiquantity_month'
predict.index.names = ['product_month', 'product_id']
predict = predict.swaplevel()
predict.to_csv('../result/prediction_lemonace_final.txt', header=True)
