import requests
from bs4 import BeautifulSoup
from urllib import parse

class Page_number:
    respones = requests.get('https://www.lyu.edu.cn/8125/list.htm')  #新闻界面的url
    respones.encoding = 'utf-8'
    html = respones.text
    soup = BeautifulSoup(html, 'html.parser')
    maxpagesnum = soup.find('em', class_='all_pages')
    nowpagenum = soup.find('em', class_='curr_page')
    Max_Pagenumber = int(maxpagesnum.text)    #最大页码
    Now_Pagenumber = int(nowpagenum.text)     #当前页码

print('最大页码：'+ str(Page_number.Max_Pagenumber)+'\n'+'当前页码：'+str(Page_number.Now_Pagenumber))