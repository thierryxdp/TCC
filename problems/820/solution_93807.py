def posLetra(frase,letra,ocorrencia):
    posocorrencia = 0
    posicao = 0
    while posicao<=len(frase):
          if str.count(frase,letra)>=ocorrencia:
             posocorrencia = posocorrencia + str.index(frase,letra)
          posicao = posicao + 1
    return posocorrencia