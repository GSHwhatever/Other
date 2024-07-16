# -*- coding:gbk -*-
from icecream import ic
from openpyxl import load_workbook
import os


class Count:

    def __init__(self) -> None:
        path = os.path.join(os.environ['USERPROFILE'], 'Desktop', '2012-2022年补贴总表.xlsx')
        self.tar_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'target.xlsx')
        self.wb = load_workbook(path)
        self.tar_wb = load_workbook(self.tar_path)
        self.tar_ws = self.tar_wb.active
        self.id_card = []

    def read(self):
        # self.tar_lis = [for i in self.tar_ws]
        # ic([[i.value for i in row] for row in self.tar_ws.rows])
        self.id_card = [i.value for i in self.tar_ws['D']]
        self.id_card.remove(('身份证号'))
        ic(self.id_card)

    def run(self):
        ws = self.wb.active
        for m, n, x, y, z in zip(ws['B'], ws['C'], ws['D'], ws['E'], ws['H']):
            l = [m.value, n.value, x.value, y.value, z.value]
            if all(l):
                l.append(f'2022-{z.value}')
                ic(l)
                self.tar_ws.append(l)
        self.tar_wb.save(self.tar_path)

    def run2(self):
        ws = self.wb.active
        for m, n, x, y, z in zip(ws['B'], ws['C'], ws['D'], ws['E'], ws['H']):
            l = [m.value, n.value, x.value, y.value, z.value]


if __name__ == '__main__':
    c = Count()
    c.read()
