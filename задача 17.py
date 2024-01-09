arr={"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"10":[],"11":[]}
with open("class.txt") as daf:
  for line in daf:
   r=line.replace('\n','').split(" ")
   arr[r[0]].append(int(r[2]))
  for k,v in arr.items():
     if len(v)==0:
       print(k," -")
     else:
       print(k,sum(v)/len(v))
