a=list(map(int,input()))
for i in range(0,len(a)):
  if i==len(a)-1:
    print(a[i],end="")
  else:
    print(a[i],end=" ")
