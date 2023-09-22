def posLetra(frase,letra,ocorrencia):
    posocorrencia = 0
    posicao = 0
    while posicao<=len(frase):
          if str.count(frase,letra)>=ocorrencia and ocorrencia == 1:
             posocorrencia = str.index(frase,letra)
          posicao = posicao + 1
          if str.count(frase,letra)>=ocorrencia and ocorrencia>1:
             posocorrencia = str.index(frase,letra,14)
          posicao = posicao + 1
          if ocorrencia>str.count(frase,letra):
              posocorrencia = -1
    return posocorrencia