# -*- coding:gbk -*-
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.utils.exceptions import InvalidFileException
from collections import Counter
from pprint import pprint
from datetime import datetime
import re

class SMZ:

    def __init__(self):
        self.header = []
        self.value_lis = []
        self.sy_values = []
        self.hyhf_list = [
            "农、林、牧、渔业",
            "采矿业",
            "制造业",
            "电力、燃气及水的生产和供应业",
            "建筑业",
            "交通运输、仓储和邮政业",
            "信息传输、计算机服务和软件业",
            "批发和零售业",
            "住宿和餐饮业",
            "金融业",
            "房地产业",
            "租赁和商务服务业",
            "科学研究、技术服务和地质勘查业",
            "水利、环境和公共设施管理业",
            "居民服务和其他服务业",
            "教育",
            "卫生、社会保障和社会福利业",
            "文化、体育和娱乐业",
            "公共管理和社会组织",
            "国际组织"
        ]
        self.cyhf_list = ['第一产业', '第二产业', '第三产业']
    
    def get_headers(self, ws, min_num, max_num):
        # 获取excel表头
        if min_num != max_num:
            # 复合表头的情况
            mer_row = [mer_cell.coord for mer_cell in ws.merged_cells.ranges if (min_num in (mer_cell.min_row, mer_cell.max_row) or max_num in (mer_cell.min_row, mer_cell.max_row))]
            # 拿到复合表头中含有合并单元格的区域
            rows_list = []
            # 对多种列名(A2,AA2,ABC2)处理
            for long in range(5, 20, 2):
                rows = [i for i in mer_row if len(i)==int(long)]
                if not rows:
                    break
                # 排序，保证表头顺序，方便直接写入一行数据
                rows.sort(key=lambda x: x.split(':')[0])
                rows_list.extend(rows)
            header = []
            for i in rows_list:
                numbers = re.findall('[0-9]+', i)
                if numbers[0] == numbers[1]:
                    # 单元格同行合并
                    start, end = re.findall('[A-Z]+', i)
                    # 列名从字母转换为数字
                    col_num1 = column_index_from_string(start[0])
                    col_num2 = column_index_from_string(end[0])
                    for n in range(col_num1, col_num2 + 1):
                        coord = get_column_letter(n) + str(int(i[1]) + 1)
                        if coord in [i[:2] for i in mer_row]:
                            continue
                        header.append(ws[coord].value.replace('\n', '').replace(' ', '').replace('（必填）', ''))

                else:
                    value = ws[i.split(':')[0]].value
                    if value:
                        header.append(value.replace('\n', '').replace(' ', '').replace('（必填）', ''))
            h2 = [i.value for i in ws[max_num]]
            if len(header) != len(h2):
                l = h2[len(header) - len(h2):]
                if None not in l:
                    header.extend(l)
        else:
            # 单行表头直接取
            header = [i.value.replace('\n', '').replace(' ', '').replace('（必填）', '') for i in ws[max_num] if i.value]
        # print(header)
        return header
    
    def syry(self, ws_sy):
        header_sy = self.get_headers(ws_sy, 2, 2)
        syry_values = []
        for row in [i for i in ws_sy.iter_rows()][2:]:
            if not row[0].value:
                break
            lis_sy = []
            for i in row:
                lis_sy.append(i.value)
            syry_values.append(dict(zip(header_sy, lis_sy)))
        keys = ['序号', '姓名', '性别', '年龄', '文化程度', '身份证号', '户籍性质', '技能特长', '就业创业证号', '是否登记失业人员', '失业人员类型', '失业时间', '领取失业保险金起止时间', '求职意向', '培训意向', '就业服务需求', '联系电话', '类型', '等级']
        for i in syry_values:
            values = []
            for key in keys:
                v = i.get(key)
                if key == '序号':
                    v = i.get('总序号')
                if key == '年龄':
                    v = datetime.now().year - int(i.get('身份证号')[6:10])
                if key == '文化程度':
                    v = i.get('学历')
                if key == '户籍性质':
                    v = '城镇'
                if key == '技能特长':
                    v = i.get('特殊技能')
                if key == '是否登记失业人员':
                    v = '是'
                if key == '失业人员类型':
                    v = '(9)'
                if key == '领取失业保险金起止时间':
                    v = '无'
                if key == '求职意向':
                    v = '服务'
                if key == '培训意向':
                    v = '无'
                if key == '就业服务需求':
                    v = '（1）'
                if key == '联系电话':
                    v = i.get('电话')
                if key == '类型':
                    v = '中短期'
                if key == '等级':
                    v = '缺乏技能' if i.get('特殊技能') == '无' else '具备技能'
                if key == '失业时间':
                    v_time = i.get('失业时间')
                    if v_time:
                        month = datetime.now().month - v.month
                        v = v_time.replace(month=datetime.now().month - 2) if month > 2 else v_time
                    else:
                        v = datetime.now().replace(month=datetime.now().month - 2, day=1, hour=0, minute=0, second=0, microsecond=0)
                values.append(v)
            self.sy_values.append(values)

    def read_file(self, file, min_num, max_num):
        # 从excel文件读取内容，将表头和内容组成字典保存在self.value_lis列表中
        # path = os.path.join(os.path.dirname(__file__), '充分就业社区基础台账', file)
        path = file
        # print(f'path:{path}')
        self.value_lis = []
        try:
            wb = load_workbook(path, data_only=True)
        except InvalidFileException as E:
            print(f'不能处理{path.split(".")[-1]}类型的Excel文件,推荐另存为xlsx类型')
            return 'error'
        else:
            if "实名制" in path.split('/')[-1] and '失业人员情况' in wb.sheetnames:
                self.syry(wb['失业人员情况'])
            try:
                ws = wb['新就业人员']
            except KeyError:
                ws = wb.worksheets[0]
            finally:
                header = self.get_headers(ws, min_num, max_num)
                for row in [i for i in ws.iter_rows()][max_num:]:
                    if not row[0].value:
                        break
                    lis = []
                    for i in row:
                        lis.append(i.value)
                    self.value_lis.append(dict(zip(header, lis)))

    def get_message(self, datas):
        # 获取台账具体信息
        syzjy = [i for i in datas if i.get('就业类型') == '失业再就业']
        jyknzjy = [i for i in datas if i.get('就业困难人员') == '是']
        dzysxl = [i for i in datas if i.get('学历') in ('大学专科', '大学本科', '硕士研究生')]
        woman = [i for i in datas if i.get('性别') == '女']
        rs1624 = [i for i in datas if int(i.get('年龄')) in range(16, 25)]
        rs2545 = [i for i in datas if int(i.get('年龄')) in range(25, 46)]
        rs4660 = [i for i in datas if int(i.get('年龄')) in range(46, 61)]
        counts = Counter([i.get('从事产业类型') for i in datas])
        cyhf = [counts.get(industry, 0) for industry in self.cyhf_list]
        counts = Counter([i.get('所属行业(就业形式为单位就业时必填)') for i in datas])
        hyhf = [counts.get(industry, 0) for industry in self.hyhf_list]
        dwjy = [i for i in datas if i.get('就业方式') == '单位就业']
        lhjy = [i for i in datas if i.get('就业方式') == '灵活就业']
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
        self.read_file(path, 2, 3)
        # ic(self.value_lis)
        dic = self.get_message(self.value_lis)
        pprint('新就业人员信息：')
        pprint(dic)
        pprint(f'失业人员个数：{len(self.sy_values)}')
        pprint(f'其中女性人数：{len([i for i in self.sy_values if "女" in i])}')


if __name__ == "__main__":
    smz = SMZ()
    smz.get_all_message(r'D:/Win7数据/D/易微扬/李建娇2024/7月/小半道社区7月新就业人员实名制.xlsx')
