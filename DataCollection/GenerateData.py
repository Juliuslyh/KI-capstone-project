from Weather.Crawler_Weather import WeatherCrawler
from Absatz.Crawler_url import UrlCrawler
import Absatz.Crawler_Absatz
from Feiertage.feiertageCheck import feiertag
from Bewertung.Crawler_Bewertung import BewertungCrawler
from Bewertung.Paragraph_to_sentence import Para_to_Sentence
import os

if __name__ == '__main__':
    BewertungCrawler()
    Para_to_Sentence()
    feiertag().load_data()
    df = WeatherCrawler().df
    df.to_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/data/'
              + 'Weather.csv')
    try:
        UrlCrawler().load_data()
    except IOError:
        print("Error: fail to get urls")
    else:
        Absatz.Crawler_Absatz.AbsatzCrawler()





