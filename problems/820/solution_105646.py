def posLetra(frase,letra,n):
  posicao=0
  i=0
  while i<len(frase):
    posicao=posicao+frase.find(letra,n)
    i=i+1