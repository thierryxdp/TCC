def conta_frases(texto):
    lista = texto
    if '.' in texto:
        lista = str.split(texto, '.')
    if '!' in texto:
         lista = str.split(texto, '!')
         
  return len(lista)