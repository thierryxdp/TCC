def maiores(ls, n):
  pos = list.find(ls, n)
  if pos < 0: # not found
    list.append(ls, n)
  list.sort(ls)
  pri = list.index(ls, n) # posição da primeira ocorrência de n
  ult = list.count(ls, n) # posição da última ocorrência de n
  del ls[: pri + ult]
  return ls