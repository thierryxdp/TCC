def maiores(l, n):
  l2 = l[:]
 
  if n not in l2: 
    list.append(l2, n) 
    list.sort(l2)     
  i = list.index(l2, n)
  return l2[:i]

  if n in l2:
    list.sort(l2)     
  i = list.index(l2, n)
  return l2[:i]