def faltante(ls):
  ls.sort()
  co = list(range(1, len(ls) + 1))
  for i in range(len(ls)):
    if co[i] < ls[i]:
      return co[i]
  return "nada faltava"