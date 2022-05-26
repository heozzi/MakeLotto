import requests
import pandas as pd
import json
import itertools


def Extract_Lotto(RootData) :
    Data = {}
    for i in range(RootData - 8, RootData + 1):
        a = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}')
        TransJson = json.loads(a.text)
        for j in range(6):
            Num = TransJson['drwtNo' + str(j + 1)]
            if Num in Data:
                Data[Num] += 1
            else:
                Data[Num] = 1

    Arr = [[] for _ in range(10)]
    for i in range(1, 46):
        if i in Data:
            Arr[Data[i]].append(i)
        else:
            Arr[0].append(i)

    for idx, i in enumerate(Arr):
        if not i: continue
        i.sort()
        print('%d개 나온 숫자 ' % idx, i)
    return Arr



if __name__ =="__main__" :
    RootData = int(input("로또 회차를 입력하세요 : "))
    a = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={RootData}')
    TransJson = json.loads(a.text)
    print(f'{RootData}회차 로또번호',' '.join(list(map(str,[TransJson['drwtNo' + str(_ + 1)] for _ in range(6)]))))

    RealData = [[] for _ in range(10)]
    for i in range(9) :
        print(RootData-i)
        RV = Extract_Lotto(RootData-i)
        for idx,_ in enumerate(RV) :
            RealData[idx].append(_)
    for idx,i in enumerate(RealData) :
        if not list(itertools.chain(*i)) : continue
        ExcelData = pd.DataFrame(data=i)
        ExcelData.to_excel(f'output/Excel_{idx}.xlsx')

