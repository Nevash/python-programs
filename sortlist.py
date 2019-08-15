n=int(input())
a=[]
for i in range(n):
 c=input()
 a.append(c)
d= sorted(a)
for x in range(len(d)):
 print(d[x], end=" ")
