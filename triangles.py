n=list(map(int,input().split()))
a=[]
for i in n:
 b=i**2
 a.append(b)
if((a[0]+a[1]==a[2]) or (a[1]+a[2]==a[0]) or (a[2]+a[0]==a[1)):
 print("yes")
else:
 print("no")
