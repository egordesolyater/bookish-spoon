with open('text.txt','r') as inf:
  tx=inf.readline().lower().split()
  arr={}
  for i in tx:
    if i not in arr:
      arr[i]=1
    else:
      arr[i]+=1
ke=0
va=0
for k,v in arr.items():
  if v>va:
    ke=k
    va=v
print(ke,va)
