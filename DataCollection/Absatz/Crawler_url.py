import pandas as pd
from requests_html import HTMLSession
from datetime import datetime
import os

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


class UrlCrawler:
    def __init__(self):
        self.url = 'https://www.statistischebibliothek.de/mir/receive/DESerie_mods_00000146'

    def load_data(self):
        session = HTMLSession()
        url = self.url
        r = session.get(url)


        def get_link_from_sel(sel):
            mylist = []
            try:
                results = r.html.find(sel)
                for result in results:
                    date = result.text
                    link = list(result.absolute_links)[0]
                    mylist.append((date, link))
                return mylist
            except:
                return None

        sel = '#main_col > div:nth-child(2) > ul > li > a'
        df_catalog = pd.DataFrame(get_link_from_sel(sel))
        df_catalog.columns = ['date', 'url']
        df_catalog = df_catalog[df_catalog.duplicated('date')==False]

        #for date in df_catalog['date']:
        #    date = '-'.join(date.split(','))
        df_catalog.to_csv(os.path.abspath(os.path.dirname(os.getcwd()))+'/data/'
                            +'url.csv')

if __name__ == '__main__':
    UrlCrawler().load_data()