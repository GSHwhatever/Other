# -*- coding:gbk -*-

from icecream import ic
import requests


class Query:

    def __init__(self) -> None:
        self.url = 'http://10.64.2.100:30010/business/m5906/entry21'        # ?aac001=&aab001=&aae140=&aac002=230304196508294612
        self.headers = {
            'Access-Token': '7cba52ef-4db0-48c8-8a27-bbc1797e7de5',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

    def query(self):
        payload = {
            "aac001": "",
            "aab001": "",
            "aae140": "",
            "aac002": "230304196508294612",
            "page": "1",
            "rows": "12"
        }
        res = requests.post(url=self.url, data=payload, headers=self.headers)
        if res.status_code == 200:
            print(res.json())
            rows = res.json().get('rows')
            if rows:
                print(rows)
                print(f'请求结果:{res.json().get("total")}条')
                # for row in rows:
                #     dic = {
                #         '个人编号': row.get('aac001'),
                #         '姓名': row.get('aac003'),
                #         '身份证号': row.get('aac002'),
                #         '单位编号': row.get('aab001'),
                #         '单位名称': row.get('aab004'),
                #         '参保身份': row.get('aac066'),
                #         '对应费款所属期': row.get('aae003'),
                #         '缴费类型': row.get('aaa115'),
                #         '费用标志': row.get('aae792'),
                #         '到账日期': row.get('aab191'),
                #         '个人实缴金额': row.get('aae082'),
                #         '数据来源': row.get('aae741')
                #     }
                #     ic(dic.values())
        else:
            print(res.status_code)
    

if __name__ == '__main__':
    Q = Query()
    Q.query()
    