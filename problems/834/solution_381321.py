def media(matriz):
  soma=0
  cont=0
  for linha in matriz:
    for n in linha:
      soma=n+soma
      contador=contador+1
  return round(soma/contador, 2)