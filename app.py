import requests
from bs4 import BeautifulSoup
import unicodecsv as csv

start = 0
result = []
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
for i in range(0, 10):
    html = requests.get('https://movie.douban.com/top250?start=' + str(start) + '&filter=', headers=header)
    # print(html.text)
    html.encoding = 'utf-8'
    start += 25
    soup = BeautifulSoup(html.text, 'html.parser')

    for item in soup.find_all('div', 'info'):
        #
        title2 = item.div.a.span.string
        # title = title2.replace('\n', ' ')
        yearline = item.find('div', 'bd').p.contents[2].string
        yearline = yearline.replace('\n', '')
        yearline = yearline.replace(' ', '')
        year = yearline[0:4]
        rating = item.find('span', {'class': 'rating_num'}).get_text()
        oneresult = [title2, rating, year]
        result.append(oneresult)
print(result)

with open('test.csv', 'wb') as f:
    w = csv.writer(f, encoding='utf-8')
    w.writerows(result)
