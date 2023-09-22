def acima_da_media(l):
  n = (sum(l)/len(l))
  l2 = l[:]
  if n not in l2: 
    list.append(l2, n) 
    list.sort(l2, reverse=True)     
  i = list.index(l2, n)
  l3 = l2[:i]
  list.reverse(l3)
  return l3