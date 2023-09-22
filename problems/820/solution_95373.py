def posLetra(frase, letra, n):
  nVezes = 0
  indice = 0
  while indice < len(frase): 
    if frase[indice] == letra: 
      nVezes += 1
      if nVezes == n: 
        return indice
  
    indice += 1
  if n > nVezes:
    return -1