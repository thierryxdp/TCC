def posLetra(frase, letra, n):
  nVezes = 0
  indice = 0 
  while indice < len(frase): 
    if frase[indice] == letra: 
      nVezes += 1
      if nVezes == n: 
        return indice
    if frase[indice] in not letra:
        return -1
    indice += 1