from PyQt5.QtWidgets import QApplication,QFileDialog
import sys,csv,numpy as np

def open_file_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header_row = next(reader)
        header_row = next(reader)
        #n = np.zeros((10000,58),dtype = np.float)
        n=np.array([])
        for row in reader:
            try:
                for i in range(58):
                    if row[i] == '-nan':
                        row[i] = 0
                    row[i] = float(row[i])
                row = np.array(row[:58])
                n = np.append(n,row,axis = 0)
            except:
                continue
        return n[0]
app = QApplication(sys.argv)
filename, filetype = QFileDialog.getOpenFileName()
#data_dic = open_file_data(filename)
#print(data_dic)
x=np.array([1,2,3])
for i in range(10):
    x = np.append(x,[1,2],axis = 0)
    print(x)
#for key,value in data_dic[22:57].items():
    #print(str(key)+': '+str(value))
    #print(key,value)