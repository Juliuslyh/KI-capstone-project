import requests
from bs4 import BeautifulSoup
import zipfile
import os
import wget
import pandas as pd
import time

pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
def AbsatzCrawler():

    def get_bierabsatz_from_urls(url):
        time.sleep(10)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.findAll('a')
        file_links = [link['href'] for link in links if "MCRZipServlet" in link['href']]
        file_links2 = [link['href'] for link in links if link['href'].endswith('pdf')]
        out_fname = 'xlsx.zip'
        if file_links2:
            for link in file_links:
                if link.split('/')[-1] != file_links2[0].split('/')[-2]:
                    wget.download(link, out=out_fname)

        else:
            wget.download(file_links[0], out=out_fname)

        zip_src=os.getcwd() + '/' + out_fname
        myzip = zipfile.ZipFile(zip_src, 'r')
        f = myzip.open(myzip.namelist()[1])
        try:
            df = pd.read_excel(f, sheet_name='Tabelle 3+4', usecols='A,B')
        except:
            try:
                df = pd.read_excel(f, sheet_name='Tab3+4', usecols='A,B')
            except:
                df = pd.read_excel(f, sheet_name='Tab.3+4', usecols='A,B')

        df = df.dropna(axis=0, how='all')
        df = df.reset_index(drop=True)
        df.columns = ['region', 'absatz(hl)']
        df['time'] = str(df['absatz(hl)'][1]) + '-' + df['absatz(hl)'][0]
        df = df.dropna(axis=0, how='any')
        df = df.reset_index(drop=True)
        f.close()
        myzip.close()
        if os.path.exists(zip_src):
            os.remove(zip_src)

        return df

    bier_list = []
    biermischung_list = []
    df_url = pd.read_csv('url.csv')
    for index, row in df_url.iterrows():
        if int(row['date'].split(',')[0]) >= 2015:
            print(row['date'])
            df = get_bierabsatz_from_urls(row['url'])
            print(df)
            bier_list.append(df[1:14])
            biermischung_list.append(df[15:28])

    df_bier = pd.concat([df for df in bier_list], ignore_index=True)
    df_biermischung = pd.concat([df for df in biermischung_list], ignore_index=True)

    df_bier.to_csv('Bierabsatz.csv')
    df_biermischung.to_csv('Absatz von Biermischungen.csv')
