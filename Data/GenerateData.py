from Weather.Crawler_Weather import WeatherCrawler
from Absatz.Crawler_url import UrlCrawler
import Absatz.Crawler_Absatz
from Feiertage.feiertageCheck import feiertag
import os

#CityList = ['Frankfurt']
#Period = [2015, 2016, 2017, 2018, 2019, 2020]

if __name__ == '__main__':
    df = WeatherCrawler().df
    df.to_csv('Weather_Frankfurt.csv')
    #UrlCrawler().load_data()
    #Absatz.Crawler_Absatz.AbsatzCrawler()
    #feiertag().load_data()




