# -*- coding:gbk -*-

import requests

class DW:

    def __init__(self) -> None:
        self.host = 'http://10.64.2.100:30010'
        self.session = requests.Session()
        self.session.headers.update({
            "Access-Token": "6eb1e770-70eb-4c7c-95ee-ba8a7c62c622",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
        })

    def test(self, name, code):
        # 基础库新增
        url = '/hljjy/lpleaf6-employment/api/aa/a/a/saveAb99'
        data = {
            "aab004": name,
            "aab301": "230000000000",
            "aab302": "黑龙江省",
            "aab998": code,
            "aae017": "230304304302",
            # "aae019": "高升",
            # "aae020": "小半道社区",
            # "aae036": "2024-08-13T02:34:13.265Z",
            # "aaf019": "高升",
            # "aaf020": "小半道社区",
            # "aaf036": "2024-08-13T02:34:13.265Z"
        }
        res = self.session.post(url=self.host + url, json=data)
        print(res.status_code)
        print(res.text)


if __name__ == "__main__":
    dw = DW()
    dw.test()
