# -*- coding:gbk -*-

from openpyxl import load_workbook
from icecream import ic
from urllib.parse import quote
from pprint import pprint
from tqdm import tqdm
import os, requests, time, re


class TY:

    def __init__(self) -> None:
        self.url = 'https://capi.tianyancha.com/cloud-tempest/web/searchCompanyV3?_=1718258637579'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
            "X-Auth-Token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc2NjY5Mzc0MSIsImlhdCI6MTcxODI0MTEzMywiZXhwIjoxNzIwODMzMTMzfQ.y_6-7CuuNwREDwMbXrV02ht69SZnHm_NpUD_GmiT3wGcL0m7kKeTgMUVu2TsHhvRVtUS_Jq7fp5tvJ5HfO0RYw",
            "X-Tycid": "1649f560292111efb3e90773fcfd9111"
        }
        self.json = {
            "cacheCode": "00230304V2020",
            "customAreaCode": "00230304V2020",
            "key": "",
            "pageNum": 1,
            "pageSize": 20,
            "referer": "search",
            "sessionNo": "1718258637.55755274",
            "sortType": "0",
            "type": "tail",
            "word": "$"
        }

    def request(self):
        res = requests.post(url=self.url, headers=self.headers, json=self.json)
        ic(res.status_code)
        if res.status_code == 200:
            data = res.json().get('data', {})
            companyList = data.get('companyList', [])
            ic(companyList)


if __name__ == "__main__":
    ty = TY()
    ty.request()
