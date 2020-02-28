import csv,pandas as pd
#定义打开csv文件的类
class OpenFile():
    # 读取index.csv 文件，获得data的索引
    def open_file_index(self):
        with open('index.csv') as f:
            reader = csv.reader(f)
            #index_dic = {},
            dic_key,dic_value = [],[]
            for row in reader:
                dic_key.append(row[2])
                dic_value.append(int(row[0].strip()))
            index_dic = dict(zip(dic_key,dic_value))
        return index_dic
    # 将字典index_dic写入到index.py中
    def write_index(self,index_dic):
        with open('index.py', 'w') as f:
            f.write(str(index_dic))
    # 读取csv_data文件
    def open_file_data(self, filename):
        frame = pd.read_csv(filename, skiprows=[0, 1, 2])
        return frame.values