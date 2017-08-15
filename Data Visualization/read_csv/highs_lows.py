import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)

    # 读取第一行数据
    header_row = next(reader)
    data = [row for row in reader]

    # 读取第二列数据（最高温度）,并转换为数字
    highs = [int(row[1]) for row in data if row[0] and row[1] and row[3]]

    # 读取第一列的日期
    dates = [datetime.strptime(row[0], "%Y-%m-%d") for row in data if row[0] and row[1] and row[3]]

    # 读取最低气温
    lows = [int(row[3]) for row in data if row[0] and row[1] and row[3]]

    # 绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", linewidth=1)
    plt.plot(dates, lows, c="blue", linewidth=1)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=15)

    # 绘制斜的日期标签
    fig.autofmt_xdate()

    plt.show()


