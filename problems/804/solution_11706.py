def eh_par(n):
  """Assuma n inteiro"""
  return (n % 2) == 0

def eh_impar(n):
  return not eh_par(n)

def filtra_pares(t):
  """Assuma que t contém 4 elementos, sempre."""
  ret = ()
  if eh_par(t[0]):
    ret = ret + (t[0],)
  if eh_par(t[1]):
    ret = ret + (t[1],)
  if eh_par(t[2]):
    ret = ret + (t[2],)
  if eh_par(t[3]):
    ret = ret + (t[3],)
  return ret