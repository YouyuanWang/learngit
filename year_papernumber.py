#!/usr/bin/env python
# coding:utf-8

import requests
import urllib
from bs4 import BeautifulSoup
import time

# 模拟header信息
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
header = {'User-Agent': user_agent}

baseUrl = 'http://xueshu.baidu.com/'
keyword = 'magnetic reconnection'  #搜索关键词


# 生成信息收集的空列表
fecthed_data = []
print '信息搜索中......'
# 循环爬取处理不同的年份的数据
for i in range(1997,2017):
    year = str(i)
    sc_year = 'sc_year={%s,%s}'%(year,year)
    data = {'wd':keyword,'tn':'SE_baiduxueshu_c1gjeupa','ie':'utf-8','filter':sc_year}
    data = urllib.urlencode(data)
    url = baseUrl+'s?'+data
    request = requests.get(url, headers=header)
    data = request.text
    # 将信息传入bs4
    soup = BeautifulSoup(data, 'html.parser')
    #print soup
    # 得到有效信息的网页
    filter_url = soup.body.div.find('span', class_='nums')
    text = filter_url.text
    #print type(text)
    fecthed_data.append(text.encode('utf-8'))
    #fecthed_data.append(text)
    # 每隔1秒请求一次，避免高频率导致封IP
    #time.sleep(1)


#将文件写入list.txt文档
file_data = open('year_papernumber.txt','w')
#file_data.writelines(fecthed_data_add_all)
for i in fecthed_data:
    if i:
        #print i
        try:
            file_data.write(i)
            file_data.write('\n')
        except UnicodeEncodeError:
            pass
file_data.close()
print '信息搜素保存完毕'
#print fecthed_data
#print type(fecthed_data[0])
#print (fecthed_data[0])


