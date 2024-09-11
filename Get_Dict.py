# -*- coding:gbk -*-
"""
获取各类下拉菜单字典接口
"""
from pprint import pprint
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'Cookie': 'SESSION=ZTcxYzNjYmQtYzUyMS00NzBmLWJmY2UtOTE1YzFiODBhYWIz; JSESSIONID=5A5583C8C9D700B0CE1696AEC32058D2',
    "Access-Token": "01a1a272-2d42-4be3-8480-e4f561f70a9b"
}
payload = {
    "businessID": "23123232"
}
code = 'aab022'
res = requests.get(url=f"http://10.64.2.100:30010/hljjy/lpleaf6-middle-basic/basic/codelist/getCodeList?type={code}", headers=headers)
print(res.status_code)
try:
    pprint(res.json()[0])
except:
    pprint(res.json())
dic = {}
for i in res.json():
    dic[i.get('value')] = i.get('name')
pprint(dic)
