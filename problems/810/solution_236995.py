def inverte(frase):
  palavras = str.split(frase)
  list.reverse(palavras)
  list.lower(palavras)
  espaco = " "
  return str.join(espaco, palavras)