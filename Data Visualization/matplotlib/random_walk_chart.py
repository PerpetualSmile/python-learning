import matplotlib.pyplot as plt

from random_walk import RandomWalk


# 绘制出随机漫步的点形成的图形
rw = RandomWalk(50000)
rw.fill_walk()

# 设置绘图窗口的尺寸
plt.figure(dpi=100, figsize=(20, 15))

# 突出起点和终点
# plt.scatter(0, 0, c="GreEn", edgecolors='None', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

point_numbers = list(range(rw.num_points))

# 绘制路径
# plt.plot(rw.x_values, rw.y_values, linewidth=2)

# 绘制每个点
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.savefig("random_walk.png", bbox_inches="tight")
plt.show()