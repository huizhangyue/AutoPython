# -*- coding: utf-8 -*-
# author： ext.zhangyue12
# datetime： 2021/3/12 13:59 
# ide： PyCharm

import xlrd


def get_excel_value(row):
    excel = xlrd.open_workbook('../test_data/testdata.xlsx')
    table = excel.sheets()[0]
    print(table.norows)  # 取总行数
    print(table.ncols)  # 取总例数
    print(table.row_values(0))  # 读取第一行的数据
    print(table.col_valuse(0))  # 读取第一列的数据
    print(table.cell_value(0, 0))  # 读取第一行的数据

    for i in range(1, table.norows):
        print(table.row_values(i))

    return table.cell_value(row, 1), table.cell_value(row, 2)
