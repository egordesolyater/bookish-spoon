with open('text.txt','r') as inf:
  tx=inf.readline()
a=''
d=''
e=''
for i in tx:
  if d=='':
    d=i
  elif i in "1234567890":
    a+=i
  else:
    e+=(d*int(a))
    d=i
    a=''
e+=d*int(a)
print(e)
