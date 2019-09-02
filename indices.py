def minimum(a, n):
 minpos=a.index(min(a))
 maxpos=a.index(max(a))
 print(minpos+1, end=" ")
 print(maxpos+1)
b=int(input())
a=list(map(int,input().split()))
minimum(a,b)
