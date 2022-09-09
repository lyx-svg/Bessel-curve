import numpy as np
import matplotlib.pyplot as plt

def cal_coefficient(points):
    num = len(points)
    coe=[]
    n = num
    for i in range(num):
        value = jiecheng(n-1)/(jiecheng(i)*jiecheng(n-1-i))
        coe.append(value)
    return coe


def jiecheng(n):
    num = 1
    if n < 0:
        print('负数没有阶乘！')
    elif n == 0:
        print('0的阶乘是1')
    else:
        for i in range(1, n + 1):
            num *= i
    return num



# points = [(0,0), (2,3), (4,5), (8,1)]
# 这里给出你需要拟合的点的集合
points = [(0,0), (8,1)]

# 产生系数
coefficient = []
coefficient = cal_coefficient(points)
# for i in range(len(coefficient)):
#     print(coefficient[i])

# 设置t的步长 我设置为0.01
step = np.arange(0, 1.01, 0.01)
# print(step)

# 计算bessel曲线
n = len(points)
x_set = []
y_set = []
# 按照每一步t循环
for i in range(len(step)):
    x = 0
    y = 0
    # 对于每次t计算出C(t)
    for j in range(len(points)):
        b = (step[i]**j)*((1-step[i])**(n-1-j))*coefficient[j]
        x += b*points[j][0]
        y += b*points[j][1]
    x_set.append(x)
    y_set.append(y)

# 可视化bessel曲线
plt.scatter(x_set, y_set)
plt.show()