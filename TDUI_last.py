import requests
import urllib
import re
import os
from bs4 import BeautifulSoup
from urllib import parse

#1.获取网站源代码
respones = requests.get('https://www.lyu.edu.cn/8125/list.htm')
respones.encoding = 'utf-8'
html = respones.text
#获取网页源代码
#print(html)
#使用BeautifulSoup 解析网页
soup = BeautifulSoup(html,'html.parser')

# print(soup.prettify())
# print(soup.column-news-title.string)

all_news = soup.find('div', class_="column-news-list clearfix")

#-------------------------------------------------------单页遍历新闻操作-------------------------------------------------

item = 1
dic = []
lst = all_news
for i in lst.find_all('a', href=True):
    dic.append(i['href'])
    # print(i['href'])
#     print(i['href'])

    class_mark = 'column-news-item item-'+str(item)+' clearfix'
    #print(class_mark)
    one_new = all_news.find('a', class_=class_mark)

    p = one_new.text
    #print(p)
    q = p[0:3]
    news_title = p[:-10]   #日期戳是10位
    news_date_text = p[-10:]
    #print(news_title)
    #print(all_news)
    news_url = "https://www.lyu.edu.cn" + dic[item-1]
    #print(news_url)
    onenews_page = news_url
    onenews_inf = requests.get(onenews_page)
    #print(onenews_page)
    onenews_inf.encoding = 'utf-8'
    onenew_html = onenews_inf.text
    #print(onenew_html)
    onenew_soup = BeautifulSoup(onenew_html,'html.parser')

    new_inf = onenew_soup.find('article', class_= "read")
    print('新闻标题：',news_title)
    print('发布时间：',news_date_text)
    print('新闻链接：',news_url)
    print('新闻内容：',new_inf.text)
    print('item = ' +str(item))



