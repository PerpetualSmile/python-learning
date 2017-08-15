import pygal

from die import Die


# 投骰子生成结果
num_sides = 6
die_1 = Die(num_sides)
die_2 = Die(num_sides)
results = [die_1.roll() + die_2.roll() for i in range(10000)]


# 统计每个点数出现的词数
frequencies = [results.count(value) for value in range(2, (num_sides * 2) + 1)]


# 可视化统计结果（直方图）
hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = range(2, 13)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6+D6", frequencies)
hist.render_to_file("die_visual.svg")

print(frequencies)
