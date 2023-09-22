def posLetra(frase,letra,ocorrencia):
    posocorrencia = 0
    posicao = 0
    while posição<=len(frase):
          if str.count(frase,letra)>=ocorrência:
             posocorrencia = posocorrencia + str.index(frase,letra)
          posicao = posicao + 1
    return posocorrencia