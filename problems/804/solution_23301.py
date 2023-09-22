def filtra_pares (a,b,c,d):
  s=""
  if(a%2 == 0):
    s = str(a)
  if(b%2 == 0):
    s = s+ str(b)
  if(c%2 == 0):
    s = s+ str (c)
  if(d%2 == 0):
    s= s+ str(d)
  return s