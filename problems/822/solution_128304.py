def repetidos(ls):
  r = [] 
  ft = ls[1: ]
  for i in range(len(ft)):
    if ft[i] == ls[i]:
      r.append( (i, i + 1) )
  return len(r)