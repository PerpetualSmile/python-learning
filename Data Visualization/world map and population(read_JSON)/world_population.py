import json
import pygal_maps_world.maps
from pygal.style import RotateStyle, LightColorizedStyle
from pygal_maps_world.i18n import COUNTRIES

from country_codes import get_country_code


# 将数据读取到列表
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 读取每个国家2010年的人口数量
cc_population = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':

        # 国家名
        country_name = pop_dict["Country Name"]

        # 人口数量有小数，因此先要转化为浮点数
        population = int(float(pop_dict["Value"]))

        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

# 根据人口数量对国家进行分组
cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    elif pop < 1000000000:
        cc_pops_3[cc] = pop
    else:
        cc_pops_4[cc] = pop

# 绘制地图
wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops_1)
wm.add("10m-100m", cc_pops_2)
wm.add("100m-1bn", cc_pops_3)
wm.add(">1bn", cc_pops_4)

wm.render_to_file("world_population.svg")
