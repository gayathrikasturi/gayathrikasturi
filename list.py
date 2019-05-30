l=list(range(100))

even=[]
for i in l:
  if i%2==0:
    even.append(i)
    
for i in even:
  l.remove(i)
print("odd:",l)
print("even:",even)