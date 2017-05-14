代码目录结构说明：
ctrip14
├─.idea  pycharm工程文件，可以忽略
│
├─data： 原始文件 
│      prediction_lilei.txt  提交样例
│      product_info.txt  产品信息表
│      product_quantity.txt  价格与销量表
│
├─make_predict  对出行产品进行预测的代码
│      main1.py  销量预测主函数
│      predict_12_23_yf.py  对销量在12到23个月之间的出行产品进行预测
│      predict_1_5.py  对销量在1到5个月之间的出行产品进行预测
│      predict_5_12.py  对销量在5到12个月之间的出行产品进行预测
│      predict_circle.py  对具有强烈周期性出行产品进行预测
│      predict_max_23.py  对具有全部销量数据的出行产品进行预测
│      predict_no.py  对没有销量数据的出行产品进行预测
│      predict_no_yf.py  对没有销量数据的出行产品进行预测
│      __init__.py  python包文件，可以忽略
│
├─pro_data  预处理获得文件
│      circle.csv  具有强周期性的出行产品历史月销量数据
│      train_district3.csv  三级地区的历史月销量数据
│      train_month.csv  出行产品的历史月销量数据
│
├─result  结果文件
│      prediction_lemonace_20170426.txt 比赛阶段提交的最佳结果
│      prediction_lemonace_final.txt 赛后复现的最佳结果与prediction_lemonace_20170426.txt保持一致
│
├─transform_data  对数据进行预处理和提取
│      circle_product.py  获取具有强周期性的出行产品历史月销量数据
│      train_district3.py  获取三级地区的历史月销量数据
│      train_month.py  获取出行产品的历史月销量数据
│      __init__.py  python包文件，可以忽略
│
└─util  辅助函数
       get_dis3_circle.py  获取具有趋势的三级地区
       get_no_tred.py  获得三级地区的趋势
       pro_is_flag.py  辅助判断函数
       __init__.py  python包文件，可以忽略
	   


	   
运行流程：
本代码主要的运行环境为：python2+（skleran、pandas、numpy、matplotlib等库）
其中具体的步骤如下：
1）运行train_month.py，获得出行产品的历史月销量数据
2）运行train_district3.py，获得三级地区的历史月销量数据
3）运行circle_product.py，获得具有强周期性的出行产品历史月销量数据
4）运行main1.py，获得最终提交结果：prediction_lemonace_final.txt



