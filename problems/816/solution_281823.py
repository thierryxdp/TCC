def maiores(ls, n):
  if n not in ls:
    list.append(ls, n)
  list.sort(ls)
  pri = list.index(ls, n) # posição da primeira ocorrência de n
  ult = list.count(ls, n) # posição da última ocorrência de n
  del ls[: pri + ult]
  return ls