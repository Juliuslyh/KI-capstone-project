import pandas as pd
from lxml import etree
import requests
import time
import logging

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

class WeatherCrawler():
    def __init__(self, CityList, Period):
        self.CityList = CityList
        self.Period = Period
        self.url1 = 'https://www.timeanddate.com/weather/germany/'
        self.url2 = '/historic?month='
        self.url3 = '&year='
        self.df = self.load_data()

    def load_data(self):
        base_url1 = self.url1
        base_url2 = self.url2
        base_url3 = self.url3
        frames = []
        for city in self.CityList:
            df_weather = pd.DataFrame(columns=["Temperature-High", "Temperature-Low", "Temperature-Average",
                                               "Humidity-High", "Humidity-Low", "Humidity-Average",
                                               "Pressure-High", "Pressure-Low", "Pressure-Average"])
            for year in self.Period:
                if year != 2020:
                    for i in range(1, 13):
                        time.sleep(10)  # 设置时间间隔为10秒
                        new_url = base_url1 + city.lower() + base_url2 + str(i) + base_url3 + str(year)
                        print(new_url)
                        res = requests.get(new_url)
                        res_elements = etree.HTML(res.text)
                        table = res_elements.xpath(
                            '/html/body/div[1]/div[6]/main/article/div[4]/div[1]')
                        print(table)
                        table = etree.tostring(table[0], encoding='utf-8').decode()
                        df = pd.read_html(table, encoding='utf-8', header=0)[0]
                        print(df)

                        dict_weather = {"Temperature-High": df['Temperature'][0],
                                        "Temperature-Low": df['Temperature'][1],
                                        "Temperature-Average": df['Temperature'][2],
                                        "Humidity-High": df['Humidity'][0], "Humidity-Low": df['Humidity'][1],
                                        "Humidity-Average": df['Humidity'][2],
                                        "Pressure-High": df['Pressure'][0], "Pressure-Low": df['Pressure'][1],
                                        "Pressure-Average": df['Pressure'][2]}

                        df_weather = df_weather.append(pd.DataFrame(dict_weather, index=[str(i) + '-' + str(year)]))
                else:
                    for i in range(1, int(time.strftime('%m', time.localtime(time.time())))):
                        time.sleep(10)  # 设置时间间隔为10秒
                        new_url = base_url1 + city.lower() + base_url2 + str(i) + base_url3 + str(year)
                        res = requests.get(new_url)
                        res_elements = etree.HTML(res.text)
                        table = res_elements.xpath(
                            '/html/body/div[1]/div[6]/main/article/div[4]/div[1]')
                        table = etree.tostring(table[0], encoding='utf-8').decode()
                        df = pd.read_html(table, encoding='utf-8', header=0)[0]

                        dict_weather = {"Temperature-High": df['Temperature'][0],
                                        "Temperature-Low": df['Temperature'][1],
                                        "Temperature-Average": df['Temperature'][2],
                                        "Humidity-High": df['Humidity'][0], "Humidity-Low": df['Humidity'][1],
                                        "Humidity-Average": df['Humidity'][2],
                                        "Pressure-High": df['Pressure'][0], "Pressure-Low": df['Pressure'][1],
                                        "Pressure-Average": df['Pressure'][2]}

                        df_weather = df_weather.append(pd.DataFrame(dict_weather, index=[str(i) + '-' + str(year)]))

            df_weather['location'] = city
            frames.append(df_weather)
        result = pd.concat(frames)
        return result
