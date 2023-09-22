def mapeia(ls, f):
  r = []
  for e in ls:
    r.append(f(e))
  return r

def reduz(it, f, init):
  r = init
  for e in it:
    r = f(r, e)
  return r

def soma_h(n):
  dn = list(range(1, n + 1))
  ts = mapeia(dn, lambda n: 1/n)
  return round(reduz(ts, lambda x, y: x + y, 0), 2)