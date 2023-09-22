def posLetra(frase,letra,numero):
    i = 0
    posicao_letra = numero
    while posicao_letra<len(frase):
          posicao_letra = numero[i]
          i = i + 1
          return posicao_letra
    else:
          return - 1