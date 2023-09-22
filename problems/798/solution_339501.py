def mapeia(it, f):
  r = []
  for e in it:
    list.append(r, f(e))
  return r
def freq_palavras(frases):
    d={}
    ps = str.split(frases)
    for p in ps:
        d[p]= dict.get(p, d, 0) + 1
    return d