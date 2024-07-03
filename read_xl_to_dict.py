# -*- coding:gbk -*-
from openpyxl import load_workbook
from collections import Counter

class SMZ:

    def __init__(self) -> None:
        self.title = {
            "xjy": ['序号', '市', '机构名称（县（区））', '姓名', '身份证号', '联系电话', '学历', '登记就业时间（年/月/日）', '就业单位(灵活就业填具体工作内容） ', '单位就业', '个体工商户', '公益性岗位', '灵活就业',
                      '失业人员再就业', '就业困难再就业', '是否录入金保', '技能等级证书', '民族', '是否是退役军人', '是否是残疾人', '社区', '年龄', '性别', '产业划分', '行业划分'],
            "sy": ['总序号', '街道序号', '姓名', '性别', '身份证号', '学历', '特殊技能', '是否登记失业人员', '失业前身份（参考05表）', '电话', '所属社区', '人员类别']
        }
        self.hyhf_list = [
            "农、林、牧、渔业",
            "采矿业",
            "制造业",
            "电力、煤气及水的生产和供应业",
            "建筑业",
            "交通运输、仓储及邮电业",
            "信息传输及计算机服务及软件业",
            "批发和零售业",
            "住宿、餐饮业",
            "金融业",
            "房地产业",
            "租赁和商务服务业",
            "科学研究、技术服务业和地质勘察",
            "水利、环境和公共设施管理",
            "居民服务和其他服务",
            "教育",
            "卫生、社会保障和社会福利业",
            "文化、体育和娱乐",
            "冰雪旅游业",
            "公共管理和社会组织",
        ]
        self.cyhf_list = ['第一产业', '第二产业', '第三产业']

    def read_file(self, sheet, tag, row_num):
        # 读取sheet表，返回字典
        row_lis = [i for i in sheet.iter_rows(values_only=True)][row_num:]
        datas = [dict(zip(self.title.get(tag), i)) for i in row_lis]
        data = [i for i in datas if i.get('身份证号')]
        # print([i.get('年龄') for i in data])
        return data

    def get_message(self, datas):
        # 获取台账具体信息
        syzjy = [i for i in datas if i.get('失业人员再就业') == '是']
        jyknzjy = [i for i in datas if i.get('就业困难再就业') == '是']
        dzysxl = [i for i in datas if i.get('学历') in ('大学专科', '大学本科', '硕士研究生')]
        woman = [i for i in datas if i.get('性别') == '女']
        rs1624 = [i for i in datas if i.get('年龄') in range(16, 25)]
        rs2545 = [i for i in datas if i.get('年龄') in range(25, 46)]
        rs4660 = [i for i in datas if i.get('年龄') in range(46, 61)]
        counts = Counter([i.get('产业划分') for i in datas])
        cyhf = [counts.get(industry, 0) for industry in self.cyhf_list]
        counts = Counter([i.get('行业划分') for i in datas])
        hyhf = [counts.get(industry, 0) for industry in self.hyhf_list]
        dwjy = [i for i in datas if i.get('单位就业') == '是']
        lhjy = [i for i in datas if i.get('灵活就业') == '是']
        # print(hyhf)
        dic = {
            "新就业人数": len(datas),
            "失业人员再就业人数": len(syzjy),
            "就业困难再就业人数": len(jyknzjy),
            "大专以上学历人数": len(dzysxl),
            "女性人数": len(woman),
            "非公有制企业": len(dwjy),
            "灵活就业": len(lhjy),
            "16-24周岁人数": len(rs1624),
            "25-45周岁人数": len(rs2545),
            "46-60周岁人数": len(rs4660),
            "产业划分": dict(zip(self.cyhf_list, cyhf)),
            "行业划分": dict(zip(self.hyhf_list, hyhf))
        }
        return dic
    
    def get_all_message(self, path):
        workbook = load_workbook(path, data_only=True)
        sheet = workbook['新就业人员']
        sheet2 = workbook['失业人员情况']
        dic = self.get_message(self.read_file(sheet, 'xjy', 3))
        datas = self.read_file(sheet2, 'sy', 2)
        woman = [i for i in datas if i.get("性别") == "女"]
        dic2 = {"失业人员": len(datas), "女性人数": len(woman)}
        print(f'失业人员信息：\n{dic2}')
        print(f'新就业人员信息：\n{dic}')


if __name__ == "__main__":
    smz = SMZ()
    smz.get_all_message('D:/易微扬/李建娇2024/2024小半道社区5月新就业人员实名制.xlsx')
