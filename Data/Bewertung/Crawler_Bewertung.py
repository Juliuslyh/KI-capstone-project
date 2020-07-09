import pandas as pd
import requests
import json

"""

"""
request_headers1 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594054849.1594067246.3; __utmt=1; __utmb=266161180.2.10.1594067246',
    'range': '0-274',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Rothaus-Pils-Tannenzaepfle',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url1 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=109'
"""

"""
request_headers2 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594076504.1594081899.6; __utmt=1; __utmb=266161180.4.10.1594081899',
    'range': '0-299',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Augustiner-Lagerbier-Hell',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url2 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=1'
"""

"""
request_headers3 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594076504.1594081899.6; __utmt=1; __utmb=266161180.6.10.1594081899',
    'range': '0-274',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Becks-Pilsner',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url3 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=160'
"""

"""
request_headers4 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594076504.1594081899.6; __utmt=1; __utmb=266161180.8.10.1594081899',
    'range': '0-199',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Jever-Pilsener',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url4 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=11'
"""

"""
request_headers5 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594076504.1594081899.6; __utmt=1; __utmb=266161180.10.10.1594081899',
    'range': '0-199',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Augustiner-Edelstoff',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url5 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=100'
"""

"""
request_headers6 = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'identity',
    'accept-language': 'zh-CN,zh;q=0.9,de;q=0.8',
    'cookie': 'PHPSESSID=f9c53982569297de4ad9f3f9dcb9c70d; __utmc=266161180; __utmz=266161180.1594052459.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=266161180.763497353.1594052459.1594076504.1594081899.6; __utmt=1; __utmb=266161180.12.10.1594081899',
    'range': '0-174',
    'range-unit': 'items',
    'referer': 'https://www.bierbasis.de/bier/Krombacher-Pils',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}
url6 = 'https://www.bierbasis.de/bb-rest/ratings/query?filter.rating.beer-id=7'


def get_data_from_url(url, request_headers):
    comments = requests.get(url, headers=request_headers).text
    data = json.loads(comments)
    datalist = []
    for i in data:
        userid = i['userId']
        comment = i['comment']
        rating = i['rating']
        dateadded = i['dateAdded']
        datalist.append([userid, comment, rating, dateadded])

    df = pd.DataFrame(datalist, columns=('userId', 'comment', 'rating', 'dateAdded'))

    return df

df1 = get_data_from_url(url1, request_headers1)
df2 = get_data_from_url(url2, request_headers2)
df3 = get_data_from_url(url3, request_headers3)
df4 = get_data_from_url(url4, request_headers5)
df5 = get_data_from_url(url5, request_headers5)
df6 = get_data_from_url(url6, request_headers6)

df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

df.to_csv('comments.csv')