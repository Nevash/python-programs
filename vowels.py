n=int(input())
n=n.lower()
c=["a", "e", "i", "o", "u"]
if(n>='a' and n<='z'):
 if n in c:
  print("Vowel")
 else:
  print("Consonant")
else:
 print("Invalid")
