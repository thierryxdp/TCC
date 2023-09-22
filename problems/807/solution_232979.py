def conta_frases(texto):
  '''Função que, ao receber um texto(texto), retorna o número de frases
  srt -> int'''
  contador = 0
  texto2=''
  if "!" in texto:
    contador+= texto.count("!")
  if "?" in texto:
    contador+= texto.count("?")
  if "..." in texto:
    texto2 = texto.replace('...','.',texto.count('...'))
  if "." in texto:
    contador+= texto2.count(".")
  return contador