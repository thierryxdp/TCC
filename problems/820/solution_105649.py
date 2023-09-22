def posLetra(frase,letra,n):
  posicao=0
  i=0
  while i<len(frase):
    if letra in frase:
        return (frase.find(letra,n))