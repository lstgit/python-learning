import pandas as pd
import xlrd


# from pandas import DataFrame


def read(file_name):
    wb = xlrd.open_workbook(filename=file_name)
    sheets = wb.sheets()
    data = {}
    for each in sheets:
        # print(each.nrows)
        nrows = each.nrows
        name = each.name
        print(name)
        list = []
        for i in range(each.nrows):
            row_data = each.row_values(i)
            # print(row_data)
            list.append(row_data)
        data[name] = list
    return data


def write(file_name):
    pass


if __name__ == '__main__':
    # data = read("C:\\Users\\lisongtao\\Documents\\javadoc\\航旅标签全量数据需求\\航旅标签全量数据需求1109.xlsx")
    # print(data)
    # data = {'name': 'lzy', 'content': '处处吻'}
    # frame = pd.DataFrame(data=data['航旅行为标签'], columns=None)
    # csv_name = "C:\\Users\\lisongtao\\Desktop\\report.csv"
    # frame.to_csv("C:\\Users\\lisongtao\\Desktop\\report.csv", index=False, encoding='gbk')
    '''
    df = pd.read_csv('C:\\Users\\lisongtao\\Desktop\\report.csv', encoding='gbk')
    print(df)
    print('*'*10)
    print(df.T)
    df = pd.read_excel('C:\\Users\\lisongtao\\Documents\\javadoc\\航旅标签全量数据需求\\航旅标签全量数据需求1109.xlsx')附表读不到
    '''
    pass
    # print(df)


