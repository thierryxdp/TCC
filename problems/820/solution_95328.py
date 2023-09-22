def posLetra(frase, letra, n):
  nVezes = 0
  indice = 0 
  while indice < len(frase): 
    if frase[indice] == letra: 
      nVezes += 1
      if nVezes == n: 
        return indice
    indice += 1
        return "A letra " + letra + " nao ocorre " + str(n) + " vezes na string"