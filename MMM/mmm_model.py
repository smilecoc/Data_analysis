# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 14:11
# @Author  : Romi的杂货铺
# @FileName: mmm_model.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel(r"C:\Users\kevin.shu\Desktop\其他工具包\Git hub 项目\Market-Mix-Modelling-master\python\MMM.xlsx")

#EDA
print (data.describe())
print (data.columns)
#查看各列的数据缺失情况
print(data.isnull().any())
print(data.isnull().any().sum())
#数据中一共有多少个品牌
print (data['BrandName'].unique())
print ('\n')
print ('Total Number of brands',len(data['BrandName'].unique()))
#选择'Absolut'作为我们的分析品牌。
Absolut = data[data['BrandName'] == 'Absolut']
Pr_Absolut = Absolut[['LnSales','LnPrice']]

#价格与销售之间的散点图
plt.scatter(Pr_Absolut['LnPrice'],Pr_Absolut['LnSales'])
plt.xlabel('Log of Price')
plt.ylabel('Log of Sales')
plt.show()

#获取回归方程与结果
import statsmodels.formula.api as sm
result = sm.ols(formula = 'LnSales ~ LnPrice',data = Pr_Absolut).fit()
result.summary()
print(result.params)
print(result.summary())

#查看回归方程的拟合情况图像
y_fitted = result.fittedvalues
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(Pr_Absolut['LnPrice'],Pr_Absolut['LnSales'], 'o', label='data')
ax.plot(Pr_Absolut['LnPrice'], y_fitted, 'r--.',label='OLS')
ax.legend(loc='best')
plt.show()

#多因素回归结果
Ad_Absolut = Absolut[['LnSales','LnMag','LnNews','LnOut','LnBroad','LnPrint','LnPrice']]
result_ad = sm.ols('LnSales ~ LnMag + LnNews + LnOut + LnBroad + LnPrint + LnPrice',data=Ad_Absolut).fit()
result_ad.summary()

#查看相关系数
print(Ad_Absolut.corr())