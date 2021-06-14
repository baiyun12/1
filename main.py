import pandas as pd
from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Map, Timeline, Line
from pyecharts.faker import Faker
import matplotlib.pyplot as plt
import numpy as np

#得到全国的疫情确诊人数数据
def data_get(month, day):
    csv = pd.read_csv("C:/Users/白云/Desktop/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/{}-{}-2021.csv".format(
        str(month).rjust(2, '0'), str(day).rjust(2, '0')))
    list_province = csv.loc[csv['Country_Region'] == 'China']['Province_State'].values.tolist()
    list_confirmed = csv.loc[csv['Country_Region'] == 'China']['Confirmed'].values.tolist()
    Dprovince = {'Anhui': '安徽', 'Beijing': '北京', 'Chongqing': '重庆', 'Guangdong': '广东', 'Guangxi': '广西', 'Guizhou': '贵州',
                 'Hainan': '海南', 'Heilongjiang': '黑龙江', 'Henan': '河南', 'Hubei': '湖北', 'Hunan': '湖南', 'Jiangxi': '江西',
                 'Jilin': '吉林', 'Liaoning': '辽宁', 'Ningxia': '宁夏', 'Shandong': '山东', 'Shanghai': '上海','Sichuan': '四川',
                 'Tianjin': '天津', 'Yunnan': '云南', 'Zhejiang': '浙江', 'Fujian': '福建', 'Gansu': '甘肃', 'Hebei': '河北',
                 'Hong Kong': '香港', 'Inner Mongolia': '内蒙古', 'Jiangsu': '江苏', 'Macau': '澳门', 'Qinghai': '青海',
                 'Shaanxi': '陕西', 'Shanxi': '山西', 'Tibet': '西藏', 'Xinjiang': '新疆'}
    for each in range(len(list_province)):
        if list_province[each] in Dprovince:
            list_province[each] = Dprovince.get(list_province[each])
    return list_province, list_confirmed

#得到中国疫情的确诊、死亡、治愈的人数数据
def get_china(i, j):
    list_confirmed_data = []
    list_death_data = []
    list_recovered_data = []
    for month in range(3, i):
        for day in range(1, j):
            confirmed_data = 0
            death_data = 0
            recovered_data = 0
            csv = pd.read_csv(
                "C:/Users/白云/Desktop/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/{}-{}-2021.csv".format
                (str(month).rjust(2, '0'), str(day).rjust(2, '0')))
            list_confirmed = csv.loc[csv['Country_Region'] == 'China']['Confirmed'].values.tolist()
            list_death = csv.loc[csv['Country_Region'] == 'China']['Deaths'].values.tolist()
            list_recovered = csv.loc[csv['Country_Region'] == 'China']['Recovered'].values.tolist()
            for each in list_confirmed:
                confirmed_data = confirmed_data + each
            list_confirmed_data.append(confirmed_data)
            for each in list_death:
                death_data = death_data + each
            list_death_data.append(death_data)
            for each in list_recovered:
                recovered_data = recovered_data + each
            list_recovered_data.append(recovered_data)
    return list_confirmed_data, list_death_data, list_recovered_data


#得到美国疫情的确诊、死亡、治愈的人数数据
def get_america(i, j):
    list_confirmed_data = []
    list_death_data = []
    list_recovered_data = []
    for month in range(3, i):
        for day in range(1, j):
            confirmed_data = 0
            death_data = 0
            recovered_data = 0
            csv = pd.read_csv(
                "C:/Users/白云/Desktop/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/{}-{}-2021.csv".format
                (str(month).rjust(2, '0'), str(day).rjust(2, '0')))
            list_confirmed = csv.loc[csv['Country_Region'] == 'US']['Confirmed'].values.tolist()
            list_death = csv.loc[csv['Country_Region'] == 'US']['Deaths'].values.tolist()
            list_recovered = csv.loc[csv['Country_Region'] == 'US']['Recovered'].values.tolist()
            for each in list_confirmed:
                confirmed_data = confirmed_data + each
            list_confirmed_data.append(confirmed_data)
            for each in list_death:
                death_data = death_data + each
            list_death_data.append(death_data)
            for each in list_recovered:
                recovered_data = recovered_data + each
            list_recovered_data.append(recovered_data)
    return list_confirmed_data, list_death_data, list_recovered_data


#得到意大利疫情的确诊、死亡、治愈的人数数据
def get_India(i, j):
    list_confirmed_data = []
    list_death_data = []
    list_recovered_data = []
    for month in range(3, i):
        for day in range(1, j):
            confirmed_data = 0
            death_data = 0
            recovered_data = 0
            csv = pd.read_csv(
                "C:/Users/白云/Desktop/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/{}-{}-2021.csv".format
                (str(month).rjust(2, '0'), str(day).rjust(2, '0')))
            list_confirmed = csv.loc[csv['Country_Region'] == 'India']['Confirmed'].values.tolist()
            list_death = csv.loc[csv['Country_Region'] == 'India']['Deaths'].values.tolist()
            list_recovered = csv.loc[csv['Country_Region'] == 'India']['Recovered'].values.tolist()
            for each in list_confirmed:
                confirmed_data = confirmed_data + each
            list_confirmed_data.append(confirmed_data)
            for each in list_death:
                death_data = death_data + each
            list_death_data.append(death_data)
            for each in list_recovered:
                recovered_data = recovered_data + each
            list_recovered_data.append(recovered_data)
    return list_confirmed_data, list_death_data, list_recovered_data



#绘制中国疫情地图
def map_china():
    pieces = [
        {"max": 99999, 'min': 10000, 'label': '10000-99999', 'color': '#8B0000'},
        {"max": 9999, 'min': 1000, 'label': '1000-9999', 'color': '#FF0000'},
        {"max": 999, 'min': 100, 'label': '100-999', 'color': '#FF4500'},
        {"max": 99, 'min': 10, 'label': '10-99', 'color': '#FFA07A'},
        {"max": 9, 'min': 1, 'label': '1-9', 'color': '#FFE4E1'},
        {"max": 0, 'min': 0, 'label': '0', 'color': '#FFFFFF'}
    ]
    tl = Timeline()
    for month in range(1, 5):
        if month == 2:
            for day in range(1, 29, 3):
                list_province, list_confirmed = data_get(month, day)
                c = (
                    Map(init_opts=opts.InitOpts(width='1000px', height='880px'))
                        .add("累计确诊人数", [list(z) for z in zip(list_province, list_confirmed)], "china")
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="中国疫情地图"),
                        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces),
                    )
    
                )
                tl.add(c, "{}月{}日".format(month, day))
        else:
            for day in range(1, 31, 3):
                list_province, list_confirmed = data_get(month, day)
                c = (
                    Map(init_opts=opts.InitOpts(width='1000px', height='880px'))
                        .add("累计确诊人数", [list(z) for z in zip(list_province, list_confirmed)], "china")
                        .set_global_opts(
                        title_opts=opts.TitleOpts(title="中国疫情地图"),
                        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True, pieces=pieces),
                    )
    
                )
                tl.add(c, "{}月{}日".format(month, day))
        
    tl.render("中国疫情地图.html")



#绘制中国的疫情综合折线图
x = []
for j in range(1, 5):
    if j==2:
        for i in range(1, 29, 5):
            x.append('{}月{}日'.format(j, i))
    else:
        for i in range(1, 31, 5):
            x.append('{}月{}日'.format(j, i))
confirmed, death, recover = get_china(5, 31)
line = (
    Line()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="confirmed", y_axis=confirmed, is_smooth=True)
        .add_yaxis(series_name="death", y_axis=death, is_smooth=True)
        .add_yaxis(series_name="recover", y_axis=recover, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="2020年1月-4月综合折线图"))
)


def three_country():
    x = np.linspace(0, 60, 60)
    # 获取三个国家的确诊，死亡，治愈人数
    china_confirmed, china_death, china_recover = get_china(5, 31)
    america_confirmed, america_death, america_recover = get_america(5, 31)
    India_confirmed, India_death, India_recover = get_India(5, 31)
    y1 = china_confirmed
    y2 = america_confirmed
    y3 = India_confirmed
    y4 = china_death
    y5 = america_death
    y6 = India_death
    # 使用plot函数绘出三个国家的确诊，死亡，治愈人数对数曲线对比图
    plt.figure()
    plt.plot(x, y1)
    plt.plot(x, y2, color='red')
    plt.plot(x, y3, color='green')
    plt.title("confirmed number contrast")
    plt.legend(['China', 'America', 'India'])
    plt.yscale("log")
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('confirmed')
    
    plt.figure()
    plt.plot(x, y4)
    plt.plot(x, y5, color='red')
    plt.plot(x, y6, color='green')
    plt.title("death number contrast")
    plt.legend(['China', 'America', 'India'])
    plt.yscale("log")
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('death')
    
    plt.figure()
    plt.plot(x, china_recover)
    plt.plot(x, america_recover, color='red')
    plt.plot(x, India_recover, color='green')
    plt.title("recover number contrast")
    plt.legend(['China', 'America', 'India'])
    plt.yscale("log")
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('recover')
    
    # 使用plot函数绘出三个国家的确诊，死亡，治愈人数对比折线图
    plt.figure()
    plt.plot(x, y1)
    plt.plot(x, y2, color='red')
    plt.plot(x, y3, color='green')
    plt.title("confirmed number contrast")
    plt.legend(['China', 'America', 'India'])
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('confirmed')
    
    plt.figure()
    plt.plot(x, y4)
    plt.plot(x, y5, color='red')
    plt.plot(x, y6, color='green')
    plt.legend(['China', 'America', 'India'])
    plt.title("death number contrast")
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('death')
    
    plt.figure()
    plt.plot(x, china_recover)
    plt.plot(x, america_recover, color='red')
    plt.plot(x, India_recover, color='green')
    plt.title("recover number contrast")
    plt.legend(['China', 'America', 'India'])
    plt.xlabel('from 2021-01-01 to 2021-04-28')
    plt.ylabel('recover')
    
    plt.show()


def main():
    map_china()
    line.render("中国综合折线图.html")
    three_country()
    
main()