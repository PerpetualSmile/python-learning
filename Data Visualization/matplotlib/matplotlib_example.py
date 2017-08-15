from matplotlib import pyplot


# matplotlib 网站http://matplotlib.org/


# pyplot.plot
x_values = list(range(-1000, 1000))
y_values = [x**2 for x in x_values]
pyplot.plot(x_values, y_values, linewidth=2)

# 设置图表标题， 并给坐标轴加上标签
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
pyplot.tick_params(axis="both", labelsize=14)


# pyplot.scatter 画点
x_values = list(range(-100, 100))
y_values = [x**3 for x in x_values]

# 颜色映射，渐变效果
pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, edgecolors="none", s=5)

# 更多访问http://matplotlib.org/, 单击Examples, 向下滚动到Color Examples, 再单击colormaps_reference


pyplot.savefig("matplotlib_example.png", bbox_inches="tight")
pyplot.show()


