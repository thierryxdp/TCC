def conta_frases(frase):
  lista_frases = frase.split(',')
  for elem in lista_frases:
    if '?' in elem:
      lista_frases += elem.split('?')
      lista_frases.remove(elem)
  for elem in lista_frases:
    if '!' in elem:
      lista_frases += elem.split('!')
      lista_frases.remove(elem)
  
  return len(lista_frases)