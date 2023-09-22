def maiores(ls, n):
  pos = list.find(ls, n)
  if pos < 0: # not found
    list.append(ls, n)
  list.sort(ls)
  pri = list.index(cp, n) # posição da primeira ocorrência de n
  ult = list.count(cp, n) # posição da última ocorrência de n
  return cp[pri + ult : ]