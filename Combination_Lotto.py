cnt = 0 #최대 개수

def dfs(n,arr,AllNumber,Number_dict,MaxVal) :
    global cnt
    if n>6:
        RV = sum([Number_dict[_] for _ in arr])
        if RV == MaxVal :
            print(arr)
            cnt+=1
        return
    for i in AllNumber :
        if i in arr : continue
        if i<=arr[-1] : continue
        dfs(n+1,arr+[i],AllNumber,Number_dict,MaxVal)

if __name__ == "__main__" :
    with open('input/LottoNumber.txt','r') as file :
        text = file.read().split('\n')

    MaxVal = int(input('값을 입력하세요 : '))
    Number_dict = {}
    AllNumber = []

    for idx,i in enumerate(text) :
        for j in i.split(',') :
            AllNumber.append(int(j))
            Number_dict[int(j)] = idx+1
    AllNumber.sort()
    for i in AllNumber :
        dfs(Number_dict[i],[i],AllNumber,Number_dict,MaxVal)
    print("모든 경우의 수 %d"%cnt)
