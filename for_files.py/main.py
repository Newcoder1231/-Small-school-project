import os
import openpyxl
os.chdir('/home/m4/Desktop/')
desk_file = openpyxl.load_workbook('tset.xlsx')
sheet1 = desk_file['Sheet1']
print(sheet1['b2'].value)