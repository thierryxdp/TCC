def freq_palavras(s):
  d = {}
  for p in s.split(" "):
    d[p] = dict.get(d, p, 0) + 1
  return d