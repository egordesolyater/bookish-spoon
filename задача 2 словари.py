def update_dictionary(d,key,value):
  if key in d.keys():
    d[key].append(value)
  elif key*2 in d.keys():
    d[key*2].append(value)
  elif key*2 not in d.keys():
    d[key*2]=[value]
