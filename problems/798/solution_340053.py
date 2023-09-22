def freq_palavras(frases):
  dic = {}
  corte = frases.split()
  for x in range(len(corte)):
    dic[corte[x]] = corte.count(corte[x])
    x += 1
  return dic