def mapeia(it, f):
  r = []
  for e in it:
    list.append(r, f(e))
  return r


def total(ls,d):
    ms=mapeia(ls,lambda s: d[s])
    return sum(ms)