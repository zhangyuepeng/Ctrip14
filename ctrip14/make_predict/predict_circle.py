# -*- coding: UTF-8 -*-


def predict_cricle(s):
    """
    对具有强周期性的出行产品进行销量预测
    :param s:历史销量
    :return: 预测的14个月销量
    """
    result = [0] * 12
    d = s[-12:].median() - s[0:12].median()
    for i in range(len(result)):
        if i == 0:
            if d < 0:
                result[i] = s[-12] * 0.8 + s[-1] * 0.2 + d / 5
            else:
                result[i] = s[-12] * 0.8 + s[-1] * 0.2 + d / 2
        else:
            if d < 0:
                result[i] = s[i + 11] * 0.7 + s[i - 1] * 0.3 + d / (5 + i)
            else:
                result[i] = s[i + 11] * 0.7 + s[i - 1] * 0.3 + d / (2 + i/2)
    result.append(result[0])
    result.append(result[1])

    return result

