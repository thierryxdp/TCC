def posLetra(frase,letra,ocorrencia):
    posocorrencia = 0
    posicao = 0
    i = 0
    while posicao<=len(frase):
          if str.count(frase,letra)>=ocorrencia and ocorrencia == 1:
             posocorrencia = str.index(frase,letra)
          posicao = posicao + 1
          if str.count(frase,letra)>=ocorrencia and ocorrencia>1:
             posocorrencia = str.index(frase,letra,i)
          posicao = posicao + 1
       i = 0
          if ocorrencia>str.count(frase,letra):
              posocorrencia = -1
    return posocorrencia