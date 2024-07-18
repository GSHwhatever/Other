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
                print(f'������:{res.json().get("total")}��')
                # for row in rows:
                #     dic = {
                #         '���˱��': row.get('aac001'),
                #         '����': row.get('aac003'),
                #         '���֤��': row.get('aac002'),
                #         '��λ���': row.get('aab001'),
                #         '��λ����': row.get('aab004'),
                #         '�α����': row.get('aac066'),
                #         '��Ӧ�ѿ�������': row.get('aae003'),
                #         '�ɷ�����': row.get('aaa115'),
                #         '���ñ�־': row.get('aae792'),
                #         '��������': row.get('aab191'),
                #         '����ʵ�ɽ��': row.get('aae082'),
                #         '������Դ': row.get('aae741')
                #     }
                #     ic(dic.values())
        else:
            print(res.status_code)
    

if __name__ == '__main__':
    Q = Query()
    Q.query()
    