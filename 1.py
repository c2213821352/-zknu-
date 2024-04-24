import csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

dataList = []


def getNewsList(fontPages, endPages, urlNumber):
    data = endPages
    for i in range(fontPages, data):
        url = "https://www.zknu.edu.cn/zsxw/list" + str(i) + "." + str(urlNumber)
        r = requests.get(url)

        if r.status_code != 200:
            raise Exception()

        html_doc = r.text
        # 解析网页
        soup = BeautifulSoup(html_doc, "html.parser")
        ul = soup.find("ul", class_='news_list list2')
        lis = ul.find_all(recursive=False)
        for index, li in enumerate(lis):
            # print(li)
            link = lis[index].find_all("span")
            text = link[0].find('a')
            text2 = link[0].get_text('title')
            print(text2.encode('latin1').decode('utf-8'))
            time = link[1].text
            print(time)
            dataList.append({'title': text2.encode('latin1').decode('utf-8'), 'date': time})


getNewsList(1, 10, "htm")
pspData = 240
for j in range(11, pspData):
    url = "https://www.zknu.edu.cn/zsxw/list" + str(j) + ".psp"
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception()

    html_doc = r.text
    # 解析网页
    soup = BeautifulSoup(html_doc, "html.parser")
    ul = soup.find("ul", class_='news_list list2')

    # for li in ul:
    #     link = li.find_all("span")
    #     text = link[0].find('a')
    #     text2 = link[0].get_text('title')
    #     print(text2.encode('latin1').decode('utf-8'))
    #     time = link[1].text
    #     print(time)
    #
    #
    lis = ul.find_all(recursive=False)
    # li1= soup.find_all("li", class_="news n1 clearfix")123
    for index, li in enumerate(lis):
        # print(li)
        link = lis[index].find_all("span")
        text = link[0].find('a')
        text2 = link[0].get_text('title')
        print(text2)
        time = link[1].text
        print(time)
        # print(index)　
        dataList.append({'title': text2, 'date': time})

# df = pd.DataFrame(dataList)

# outputpath = 'C:/Users/changleqi/Desktop/py/py/data.csv'
# df.to_csv(outputpath, sep=',', index=False)
# 将DataFrame对象写入CSV文件
# df.to_csv('data.csv', index=False)
fields = ['title', 'date']
with open('data.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fields)

    # 写入字段名
    writer.writeheader()
    # 写入数据
    writer.writerows(dataList)

print('数据已成功写入CSV文件')
