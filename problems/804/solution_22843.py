def filtra_pares(a,b,c,d):
  numero = (a,b,c,d)
  palavra =''
  for c in numero:
    if c %2==0:
      palavra+=str(c)
      palavra+=" "
  pares = tuple(palavra.split())
  return pares