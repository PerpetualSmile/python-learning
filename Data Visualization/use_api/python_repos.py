"""抓取github上有关python的项目， 按照星标数排行，点击对应柱状图可以跳到该项目的github页面"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并且存储响应
url = r"https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 存储API响应
respose_dict = r.json()
print("Total repositories:", respose_dict["total_count"])

# 探索有关仓库的信息
repo_dicts = respose_dict["items"]
print("Respositories returned:", len(repo_dicts))


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    plot_dict = {
        "value": repo_dict["stargazers_count"],
        "label": str(repo_dict["description"]),
        # 添加超链接
        "xlink": repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)


# 数据可视化

    # 设置图表样式
    my_style = LS("#336699", base_style=LCS)
    my_config = pygal.Config()

    # x_label_rotation=45 让标签绕x轴旋转45度
    my_config.x_label_rotation = 45

    # show_legend=False 不显示图例
    my_config.show_legend = False

    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    # 将较长的项目名缩短为15字符
    my_config.truncate_label = 15
    # 隐藏水平线
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = "Most-Starred Python Projects on Github"
    chart.x_labels = names

    # 不添加标签
    chart.add("", plot_dicts)

    chart.render_to_file("python_repos.svg")

    # print("\nName:", repo_dict["name"])
    # print("Owner:", repo_dict["owner"])
    # print("Stars:", repo_dict["stargazers_count"])
    # print("Repository:", repo_dict["html_url"])
    # print("Created:", repo_dict["created_at"])
    # print("Update:", repo_dict["updated_at"])
    # print("Description:", repo_dict["description"])

