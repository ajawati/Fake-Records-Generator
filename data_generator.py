import sys
import random
import xlsxwriter
from faker import Faker
import pandas as pd
import secrets
#import os

#os.chdir('D:\python\Records_Generator')
clarg = sys.argv
print('Reading Data From: ', clarg[1])
print('Number of records: ', clarg[2])

col_headers = list()
rows = dict()

df = pd.read_excel(clarg[1])
col_headers = df.columns
for header in col_headers:
    rows[header] = df[header][0]

workbook = xlsxwriter.Workbook('Generator_Data.xlsx')
worksheet = workbook.add_worksheet()

len_header = len(col_headers)
row_count = int(clarg[2])

header_itr = 0
fake = Faker()

for key in rows:
    worksheet.write(0, header_itr, key)
    if rows[key] == 'number':
        for i in range(1, row_count+1):
            worksheet.write(i,header_itr, random.choice(list(range(row_count))))
    elif rows[key] =='country':
        for i in range(1, row_count + 1):
            worksheet.write(i, header_itr, fake.country())
    elif rows[key] == 'email':
        for i in range(1, row_count + 1):
            worksheet.write(i, header_itr, fake.email())
    elif rows[key] == 'name':
        for i in range(1, row_count + 1):
            worksheet.write(i, header_itr, fake.first_name())
    elif rows[key] == 'token':
        for i in range(1, row_count + 1):
            worksheet.write(i, header_itr, secrets.token_hex(5))
    elif str(rows[key]).startswith('age'):
        value_str = str(rows[key][4:len(str(rows[key]))-1:1])
        value_list = value_str.split(',')
        for i in range(1, row_count + 1):
            worksheet.write(i, header_itr, random.choice(value_list))
    header_itr+= 1

workbook.close()




