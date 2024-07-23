# -*- coding:gbk -*-

from icecream import ic
import requests


class Query:

    def __init__(self) -> None:
        self.url = 'http://10.64.2.100:30010/business/m5908/entry21'        # ?aac001=&aac002=230304196508294612&aab001=&aae042=&aae041=
        self.headers = {
            'Access-Token': 'a0bfc75e-30ed-4ecc-92d2-f26e1a195f52',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

    def query(self, ids, year):
        payload = {
            "aac001": "",			        # 个人编号
            "aac002": ids,	# 社会保障号
            "aab001": "",   		        # 单位编号
            "aae042": f"{year}12",		        # 终止年月
            "aae041": f"{year}01",		        # 开始年月	
            "page": "1",
            "rows": "30"
        }
        res = requests.post(url=self.url, data=payload, headers=self.headers)
        if res.status_code == 200:
            # print(res.json())
            error = res.json().get('error')
            rows = res.json().get('rows')
            if isinstance(rows, list) and not error:
                print(f'请求结果:{res.json().get("total")}条')
                for row in rows:
                    dic = {
                        '个人编号': row.get('aac001'),
                        '姓名': row.get('aac003'),
                        '身份证号': row.get('aac002'),
                        '单位编号': row.get('aab001'),
                        '单位名称': row.get('aab004'),
                        '参保身份': row.get('aac066'),
                        '对应费款所属期': row.get('aae003'),
                        '缴费类型': row.get('aaa115'),
                        '费用标志': row.get('aae792'),
                        '到账日期': row.get('aab191'),
                        '个人实缴金额': row.get('aae082'),
                        '数据来源': row.get('aae741')
                    }
                    ic(dic.values())
            else:
                print(f'{ids}-{error}')
        else:
            print(res.status_code)
    
    def read(self):
        from openpyxl import load_workbook
        wb = load_workbook(r'C:/Users/XBD/Desktop/大半道查询.xlsx')
        ws = wb['Sheet1']
        id_card = [i.value for i in ws['E']][2:82]
        for ids in id_card:
            self.query(ids, '2022')
    

if __name__ == '__main__':
    Q = Query()
    # Q.read()
    Q.query('230304197202034441', '2022')

