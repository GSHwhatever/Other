# -*- coding:gbk -*-
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Token": "c8fdb757-44e0-4d36-acb5-cb204123e792",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "JSESSIONID=7369AF6B88D2842E0A7DC57620F4F0F7; SESSION=YjRjMmNiMjktNzM1Ni00YTM0LTkxNTgtNWQxNzg0MGFlN2Nm",
    "Host": "10.64.2.100:30010",
    "Origin": "http://10.64.2.100:30010",
    # "Referer": "http://10.64.2.100:30010/hljjy/hljjyui/aa/b/a/aaba.html?token=c01472f5-5050-42f7-842e-053bc674e698&sa0200=608002521&sa0201=%E4%B8%AA%E4%BA%BA%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF%E7%BB%B4%E6%8A%A4",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36"
}

headers2 = {
    
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Token": "c8fdb757-44e0-4d36-acb5-cb204123e792",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "JSESSIONID=7369AF6B88D2842E0A7DC57620F4F0F7; SESSION=YjRjMmNiMjktNzM1Ni00YTM0LTkxNTgtNWQxNzg0MGFlN2Nm",
    "Host": "10.64.2.100:30010",
    "Origin": "http://10.64.2.100:30010",
    "Referer": "http://10.64.2.100:30010/hljjy/hljjyui/aa/b/a/aaba.html?token=c01472f5-5050-42f7-842e-053bc674e698&sa0200=608002521&sa0201=%E4%B8%AA%E4%BA%BA%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF%E7%BB%B4%E6%8A%A4",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36"
}

data1 = {"aac002":"230304199312284416"}
bh = ''
res = requests.post(url='http://10.64.2.100:30010/hljjy/lpleaf6-employment/api/aa/b/a/queryAc01Page?pageNo=1', headers=headers2, json=data1)
print(res.status_code)
print(res.json())
datas = res.json().get('data')
if datas:
    lis = datas.get('list')
    if lis:
        bh = lis[0].get('aac001')

print(f'bh:{bh}')

res1 = requests.post(url=f'http://10.64.2.100:30010/hljjy/lpleaf6-employment/api/aa/b/a/getAc01ById?aac001={bh}', headers=headers)
print(res1.status_code)

data = res1.json().get('data')
data['aae020'] = "小半道社区"
print(data)

res2 = requests.post(url="http://10.64.2.100:30010/hljjy/lpleaf6-employment/api/aa/b/a/saveAc01", headers=headers2, json=data)
print(res2.status_code)
print(res2.json())
