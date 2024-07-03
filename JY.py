# -*- coding:gbk -*-
# 实名制导入手动校验
import requests

class I:

    def __init__(self) -> None:
        self.host = 'http://10.64.2.100:30010'
        self.session = requests.session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "Access-Token": '37ef6ab5-07ab-4861-90a4-304bdfe0eb56'
        })

    def req(self):
        # 230304304302小半道
        # 230304304307立井
        # 230304304304白灰窑
        # 230304304301大半道
        dic = {
            "aae017": "230304304302",
            "acc033Query": [],
            "pageNo": 1,
            "pageSize": 10
        }
        res = self.session.post(url=self.host + '/hljjy/lpleaf6-employment/api/cb/d/a/queryCc03New', json=dic)
        if res.status_code==200:
            lis = res.json().get('list', [])
            # print(lis)
            for d in lis:
                print(d.get('aac003'))
                res2 = self.session.post(url=self.host + '/hljjy/lpleaf6-employment/api/cb/d/a/modifyCc03New', json=d)
                print(res2.status_code)


if __name__ == '__main__':
    i = I()
    i.req()
        
    