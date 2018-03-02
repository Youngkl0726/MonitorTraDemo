# -*- coding: utf-8 -*-
import numpy as np

from sklearn import linear_model

import matplotlib.pyplot as plt


# xx, yy = np.meshgrid(np.linspace(0,10,10), np.linspace(0,100,10))
# print("xx is: {}, yy is: {}".format(xx, yy))
# zz = 1.0 * xx + 3.5 * yy + np.random.randint(0,100,(10,10))

# 构建成特征、值的形式
cor_pic = [[595, 535], [1324, 450], [479, 612], [1451, 482]]
cor_world = [[66,18], [56,22], [67,14], [54,20]]
X = np.array(cor_pic)
Z1 = []
Z2 = []
for i in xrange(4):
    Z1.append(cor_world[i][0])
for i in xrange(4):
    Z2.append(cor_world[i][1])
print Z1, Z2
# X, Z = np.column_stack((xx.flatten(),yy.flatten())), zz.flatten()
print("X is: {}, shape is: {}".format(X, X.shape))
# print("Z is: {}, shape is: {}".format(Z, X.shape))
# 建立线性回归模型
regr = linear_model.LinearRegression()

# 拟合
regr.fit(X, Z1)

# 不难得到平面的系数、截距
a1, b1 = regr.coef_, regr.intercept_
# a1 = [[-0.01293361],[0.00503619]]
# b1 = [71.3534186032]
print("a is: {}, b is: {}".format(a1,b1))
# 给出待预测的一个特征
x1 = np.array([[66.625,843.188]])
x2 = np.array([[1717.81,388.43]])
# print(regr.predict(x))
# 方式1：根据线性方程计算待预测的特征x对应的值z（注意：np.sum）
print(np.sum(a1 * x1) + b1)
print(np.sum(a1 * x2) + b1)

regr.fit(X, Z2)
a2, b2 = regr.coef_, regr.intercept_
# a2 = [[-0.00024344],[-0.03693893]]
# b2 = [34.859918688]
print("a is: {}, b is: {}".format(a2,b2))
# 方式2：根据predict方法预测的值z
# print(regr.predict(x))
print(np.sum(a2 * x1) + b2)
print(np.sum(a2 * x2) + b2)


# 画图
# fig = plt.figure()
# ax = fig.gca(projection='3d')

# 1.画出真实的点
# ax.scatter(xx, yy, zz)

# 2.画出拟合的平面
# ax.plot_wireframe(xx, yy, regr.predict(X).reshape(10,10))
# ax.plot_surface(xx, yy, regr.predict(X).reshape(10,10), alpha=0.3)


# plt.show()