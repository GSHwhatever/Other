from faker import Faker
from openpyxl import load_workbook


fake = Faker("zh_CN")
path = r'C:\Users\XBD\Desktop\phone.xlsx'
wb = load_workbook(path)
ws = wb.active
for i in range(1, 11):
    print(fake.phone_number())
    ws.append([i, fake.phone_number(), '', ''])

wb.save(path)
