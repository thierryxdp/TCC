def posLetra(frase,letra,ocorrencia):
    posicao = 0
    posocorrencia = 0
    while posicao<len(frase) and str.count(frase,letra)>=ocorrencia:
          posocorrencia = posocorrencia + str.index(frase,letra)
          posicao = posicao + 1 
    return posocorrencia