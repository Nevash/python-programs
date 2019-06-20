string=input("Enter the string ")
string=string.lower()
n=len(string)
l=[]
if(n>=1 and n<=100000):
    for i in range(0,n):
       if(string[i]!=" " and string[i] not in l ):
            l.append(string[i])
            count=len(l)
print(count)
