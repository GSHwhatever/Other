# -*- coding:gbk -*-
"""
�𱣵�¼�ӿ�
"""
from requests.exceptions import RequestException, ConnectionError, Timeout, TooManyRedirects
import requests, time, os, json


class Login:

    def __init__(self) -> None:
        self.host = 'http://10.64.2.100:30010'

    def auth(self, name=None, idcard=None):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "51",
            "Content-Type": "application/x-www-form-urlencoded",
            # "Cookie": "SESSION=ZTcxYzNjYmQtYzUyMS00NzBmLWJmY2UtOTE1YzFiODBhYWIz; JSESSIONID=5A5583C8C9D700B0CE1696AEC32058D2",
            "Host": "10.64.2.100:30010",
            "If-Modified-Since": "0",
            "Origin": self.host,
            "Pragma": "no-cache",
            "Referer": self.host + "/portal/login.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.login_dic = {
            'id': '230304200003034021',
            'name': '����'
        }
        payload = {
            "aac002": idcard if idcard else self.login_dic.get('id'),
            "aac003": name if name else self.login_dic.get('name')
        }
        url = self.host + '/portal/queryUserInfoWithChannel'
        res = requests.post(url=url, data=payload, headers=headers)
        if res.status_code == 200:
            print(res.text)
            return res.json()

    def login(self, dic):
        h_headers = {
            "Host": "10.64.2.100:30010",
            "Content-Length": "71",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Authorization": "Basic amJ4cHQ6c3lzdGVt",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
            "Content-Type": "application/json",
            "Origin": "http://10.64.2.100:30010",
            "Referer": "http://10.64.2.100:30010/portal/login.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "JSESSIONID=474C958FD8A4B85110CF1B3D92C42BC6; SESSION=OTZiZjM4MTQtYzhhOC00Mjk1LWExMjMtZDdjNGU3NTBhMTFm",
            "Connection": "keep-alive"
        }
        session = requests.Session()
        session.headers.update(h_headers)
        payload_login = {
            "username": dic.get('ua0100'),
            "password": dic.get('ua0102')
        }
        # print(payload_login)
        url_login = self.host + '/api/auth/channel/login'
        res_login = session.post(url=url_login, data=json.dumps(payload_login).replace(' ',''), headers=h_headers)
        if res_login.status_code == 200:
            return res_login.json()
        else:
            print(res_login.status_code)
            print(res_login.text)

    def write_Acces_Token(self, token):
        path = os.path.join(os.path.dirname(__file__), 'config')
        if not os.path.exists(path):
            os.mkdir(path)
        with open(os.path.join(path, 'Access-Token.txt'), 'w') as f:
            f.write(token)

    def run(self, idcard=None, name=None):
        dic = self.auth(name=name, idcard=idcard)
        if dic:
            r = self.login(dic)
            # print(r)
            if r.get('msg')  == "��½�ɹ�":
                token = r.get('map').get('Access-Token')
                self.write_Acces_Token(token)
                tar_name = name if name else self.login_dic.get("name")
                print(f'{tar_name}��¼�ɹ�-{token}')
            else:
                print('��¼ʧ��')
        else:
            print("��¼ʧ��")
    
    def main(self, *arg, **kwargs):
        try:
            self.run(*arg, **kwargs)
        except ConnectionError as e:
            print('\n���Ӵ���\n', '\t���Ϸɻ�����?�ͽ𱣵�¼����С��')
        except Timeout as e:
            print('\n���ӳ�ʱ��\n', '\t������')
        except TooManyRedirects as e:
            print('�ض���������ࣺ', e)
        except RequestException as e:
            print('�����쳣��', e)
        else:
            pass


if __name__ == "__main__":
    l = Login()
    # l.main(name='����', idcard='230304198302014020')
    # l.main(name='��ӱ', idcard='230304199910264423')
    # l.main(name='�Ź���', idcard='230304199509154033')
    # l.main(name='����', idcard='230304199203194622')
<<<<<<< HEAD
    l.main(name='����', idcard='230304199812134414')
=======
    # l.main(name='����', idcard='230304199812134414')
>>>>>>> 43137012a615d61b42b94bd2b5a515651ecd7650
    l.main(name='����', idcard='230304200003034021')
    # l.main()
