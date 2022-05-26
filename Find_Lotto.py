import pandas as pd

Input_PATH = 'output/'

if __name__ == "__main__" :
    Data = []
    for i in range(10) :
        Excel = pd.read_excel(Input_PATH+'Excel_%d.xlsx'%i)
        Excel = Excel.fillna('')

        for j in Excel.values :
            tmp = [int(_) for _ in j[1:] if _ ]
            Data.append(tmp)
        # print(Data)
        break

    for i in range(len(Data)) :
        for j in range(len(Data[i])) :
            C1,C2 =False,False
            if i >=1 :
                RV =0
                if Data[i][j] in Data[i-1] : RV = Data[i-1].index(Data[i][j])
                if abs(j-RV) >=2 : C1 = True
            else : C1 = True
            if i<len(Data)-1 :
                RV = 0
                if Data[i][j] in Data[i+1] : RV = Data[i+1].index(Data[i][j])
                if abs(j-RV) >=2 : C2 = True
            else : C2 = True
            if C1 and C2 : print(Data[i][j],end=' ')
        print()