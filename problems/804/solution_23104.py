def filtra_pares(a,b,c,d):
  par = []
  if a % 2 == 0:
    par.append(a)
  if b % 2 == 0:
    par.append(b)
  if c % 2 == 0:
    par.append(c)
  if d % 2 == 0:
    par.append(d)
  t = tuple(par)
  
  return t