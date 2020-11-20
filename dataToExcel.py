import xlrd
import xlsxwriter

class DTE:


    def __init__(self,fileName):
        self.outPut = fileName+'.xlsx'

    def write(self, DATA):

        workbook = xlsxwriter.Workbook(self.outPut)  # 创建一个Excel文件
        worksheet = workbook.add_worksheet()  # 创建一个sheet
        # title = [U'UE',U'D2D',U'sum', U'UE', U'D2DOwn', U'D2DPublic', U'averageUE', U'averageD2DOwn', U'averageD2DPublic']  # 表格title
        title = [U'UE' ]  # 表格title
        worksheet.write_row('A1', title)  # title 写入Excel


        for i in range(len(DATA)):
            Steps = i + 2
            num = str(Steps)
            row = 'A' + num
            # data = [Data0[i],Data1[i],Data2[i],Data3[i],Data4[i],Data5[i],Data6[i],Data7[i],Data8[i]]
            data = [DATA[i]]
            worksheet.write_row(row, data)
        workbook.close()





