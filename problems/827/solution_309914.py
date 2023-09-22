def filtra(ls, p):
  r = []
  for e in ls:
    if p(e):
      r.append(e)
  return r

def mapeia(ls, f):
  r = []
  for e in ls:
    r.append(f(e))
  return r

def qtd_divisores(n):
  ls = list(range(1, n + 1))
  ds = mapeia(ls, lambda x: (x, n % x == 0))
  fs = filtra(ds, lambda t: t[1])
  return len(fs)