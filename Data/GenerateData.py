from Weather.Crawler import WeatherCrawler
import os

CityList = ['Darmstadt', 'Frankfurt']
Period = [2015, 2016, 2017, 2018, 2019, 2020]

if __name__ == '__main__':
    df = WeatherCrawler(CityList, Period).df
    df.to_csv(os.getcwd()+'/Databank/Weather.csv')
