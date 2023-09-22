def conta_frases(frase):
    ponto = frase.replace('!', '.').replace('?', '.').replace('...', '.')
    lista = ponto.split('.')
  return len(lista)