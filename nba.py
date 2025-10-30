import lxml 
import requests
from lxml import etree
url='https://nba.hupu.com/stats/players'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
e=etree.HTML(resp.text)
nos=e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names=e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams=e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores=e.xpath('//table[@class="players_table"]//tr/td[4]/text()')
with open('nba.txt','w',encoding='utf-8') as f:
    for no,name,team,score in zip(nos,names,teams,scores):
        f.write(f'排名: {no}  姓名:{name}  球队:{team}  得分:{score}\n')
