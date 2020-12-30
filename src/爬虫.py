import requests
import re
from time import sleep
# 浏览器头部

x ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
# 发送请求
a = requests.get(url = 'https://www.zhipin.com/c101280600-p100309/?ka=search_100309')
# 将获取的响应数据赋给变量b
b = a.content.decode(encoding = 'utf-8')# encoding = 'gbk' 是该网页的编码方式
print(b)# 打印获取到的数据
# a1 = re.compile(r'<a href="(.*?)" rel="nofollow">(.*?)</a>')# 编写正则规则
# b1 = re.findall(a1,b)# 使用正则规则a1去匹配字符串b中的内容
# # print(b1)
# txt = open(file='废物豪婿韩三千.txt',mode='a',encoding='utf-8')
# for i in b1:
#     print(i)
#     txt.write(f'{i}\n')
#     sleep(5)
