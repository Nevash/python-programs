def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    repeated=sorted(repeated)
    repeated=str(repeated)
    return str(repeated)[1:] 
n=int(input())
list1=[]
for i in range(0,n):
    ele=input()
    list1.append(ele)
print (Repeat(list1))
