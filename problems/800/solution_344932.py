def freq_palavras(frases):

  dicionário = {}
  repetições = 0

  for palavra in frases.split(" "):
    repetições = list.count(frases.split(" "),palavra)
    dicionário[palavra] = repetições
  return dicionário