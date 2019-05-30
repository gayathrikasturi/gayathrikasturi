d1 = {1:"one", 2:"two"}
d2 = {2:"two", 3:"three", 4:"four"}
x=[]
y=[]
z=[]
for a in d1:
  if a not in d2:
    x.append(a)
  else: 
     z.append(a)
for a in d2:
    if a not in d1:
     y.append(a)
print(x)
print(y)
print(z)
