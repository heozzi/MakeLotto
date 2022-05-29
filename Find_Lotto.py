import itertools
import pandas as pd

Input_PATH = 'output/'
#TODO 1.퍼펙트 숫자 찾기
#1) 9개 숫자가 다 나옴
#2) 8개는 나오는데 마지막 숫자만 레벨업

if __name__ == "__main__" :
    House_li = {} #동네
    Perfect_li = [] # 퍼펙트수
    NextPerfect = [] # 다음 퍼펙트 수
    for n in range(6) :
        Data = []
        Excel = pd.read_excel(Input_PATH+'Excel_%d.xlsx'%n)
        Excel = Excel.fillna('')

        for j in Excel.values :
            tmp = [int(_) for _ in j[1:] if _ ]
            Data.append(tmp)


        print("%d 오목수 찾기"%n)
        for i in range(len(Data)) :
            print('%d회 : '%(i+1),end=' ')
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
        print('='*25)
        # print('퍼펙트 수 찾기')

        FlattenData = list(itertools.chain(*Data))
        FlattenData = list(set(FlattenData))
        FlattenData.sort()

        if NextPerfect :
            for P in NextPerfect :
                if P in Data[-1] : Perfect_li.append(P)
        NextPerfect.clear()

        for P in FlattenData :
            if P in House_li : House_li[P].append(n)
            else : House_li[P] = [n]
            Perfect = len([1 for i in Data if P in i])
            if Perfect == 9 : Perfect_li.append(P)
            elif Perfect == 8 : NextPerfect.append(P)
    Perfect_li.sort()
    print('퍼펙트 수 : ',Perfect_li)
    print('동네 찾기 :', end=' ')
    for i in House_li :
        if len(House_li[i]) >=4 : print(i,end=' ')