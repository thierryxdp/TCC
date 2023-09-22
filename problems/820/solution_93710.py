import math
def posLetra(frase,letra,ocorrencia):
    posicao = 0
    posocorrencia = 0
    while posicao<len(frase) and str.count(frase,letra)>=ocorrencia:
          posocorrencia = math.ceil((posocorrencia + str.index(frase,letra))/len(frase))
          posicao = posicao + 1 
    return posocorrencia