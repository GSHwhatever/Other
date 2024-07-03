# -*- coding:gbk -*-
from openpyxl import load_workbook
from collections import Counter

class SMZ:

    def __init__(self) -> None:
        self.title = {
            "xjy": ['���', '��', '�������ƣ��أ�������', '����', '���֤��', '��ϵ�绰', 'ѧ��', '�ǼǾ�ҵʱ�䣨��/��/�գ�', '��ҵ��λ(����ҵ����幤�����ݣ� ', '��λ��ҵ', '���幤�̻�', '�����Ը�λ', '����ҵ',
                      'ʧҵ��Ա�پ�ҵ', '��ҵ�����پ�ҵ', '�Ƿ�¼���', '���ܵȼ�֤��', '����', '�Ƿ������۾���', '�Ƿ��ǲм���', '����', '����', '�Ա�', '��ҵ����', '��ҵ����'],
            "sy": ['�����', '�ֵ����', '����', '�Ա�', '���֤��', 'ѧ��', '���⼼��', '�Ƿ�Ǽ�ʧҵ��Ա', 'ʧҵǰ��ݣ��ο�05��', '�绰', '��������', '��Ա���']
        }
        self.hyhf_list = [
            "ũ���֡�������ҵ",
            "�ɿ�ҵ",
            "����ҵ",
            "������ú����ˮ�������͹�Ӧҵ",
            "����ҵ",
            "��ͨ���䡢�ִ����ʵ�ҵ",
            "��Ϣ���估������������ҵ",
            "����������ҵ",
            "ס�ޡ�����ҵ",
            "����ҵ",
            "���ز�ҵ",
            "���޺��������ҵ",
            "��ѧ�о�����������ҵ�͵��ʿ���",
            "ˮ���������͹�����ʩ����",
            "����������������",
            "����",
            "��������ᱣ�Ϻ���ḣ��ҵ",
            "�Ļ�������������",
            "��ѩ����ҵ",
            "��������������֯",
        ]
        self.cyhf_list = ['��һ��ҵ', '�ڶ���ҵ', '������ҵ']

    def read_file(self, sheet, tag, row_num):
        # ��ȡsheet�������ֵ�
        row_lis = [i for i in sheet.iter_rows(values_only=True)][row_num:]
        datas = [dict(zip(self.title.get(tag), i)) for i in row_lis]
        data = [i for i in datas if i.get('���֤��')]
        # print([i.get('����') for i in data])
        return data

    def get_message(self, datas):
        # ��ȡ̨�˾�����Ϣ
        syzjy = [i for i in datas if i.get('ʧҵ��Ա�پ�ҵ') == '��']
        jyknzjy = [i for i in datas if i.get('��ҵ�����پ�ҵ') == '��']
        dzysxl = [i for i in datas if i.get('ѧ��') in ('��ѧר��', '��ѧ����', '˶ʿ�о���')]
        woman = [i for i in datas if i.get('�Ա�') == 'Ů']
        rs1624 = [i for i in datas if i.get('����') in range(16, 25)]
        rs2545 = [i for i in datas if i.get('����') in range(25, 46)]
        rs4660 = [i for i in datas if i.get('����') in range(46, 61)]
        counts = Counter([i.get('��ҵ����') for i in datas])
        cyhf = [counts.get(industry, 0) for industry in self.cyhf_list]
        counts = Counter([i.get('��ҵ����') for i in datas])
        hyhf = [counts.get(industry, 0) for industry in self.hyhf_list]
        dwjy = [i for i in datas if i.get('��λ��ҵ') == '��']
        lhjy = [i for i in datas if i.get('����ҵ') == '��']
        # print(hyhf)
        dic = {
            "�¾�ҵ����": len(datas),
            "ʧҵ��Ա�پ�ҵ����": len(syzjy),
            "��ҵ�����پ�ҵ����": len(jyknzjy),
            "��ר����ѧ������": len(dzysxl),
            "Ů������": len(woman),
            "�ǹ�������ҵ": len(dwjy),
            "����ҵ": len(lhjy),
            "16-24��������": len(rs1624),
            "25-45��������": len(rs2545),
            "46-60��������": len(rs4660),
            "��ҵ����": dict(zip(self.cyhf_list, cyhf)),
            "��ҵ����": dict(zip(self.hyhf_list, hyhf))
        }
        return dic
    
    def get_all_message(self, path):
        workbook = load_workbook(path, data_only=True)
        sheet = workbook['�¾�ҵ��Ա']
        sheet2 = workbook['ʧҵ��Ա���']
        dic = self.get_message(self.read_file(sheet, 'xjy', 3))
        datas = self.read_file(sheet2, 'sy', 2)
        woman = [i for i in datas if i.get("�Ա�") == "Ů"]
        dic2 = {"ʧҵ��Ա": len(datas), "Ů������": len(woman)}
        print(f'ʧҵ��Ա��Ϣ��\n{dic2}')
        print(f'�¾�ҵ��Ա��Ϣ��\n{dic}')


if __name__ == "__main__":
    smz = SMZ()
    smz.get_all_message('D:/��΢��/���2024/2024С�������5���¾�ҵ��Աʵ����.xlsx')
