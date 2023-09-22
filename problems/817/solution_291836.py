def acima_da_media(l):
  n1 =(int(l)/len(l))
  n = list.int(n1)
  l2 = l[:]
  list.append(l2, n) 
  list.sort(l2)    
  i = list.index(l2, n)
  l3 = l2[i:]
  return l3