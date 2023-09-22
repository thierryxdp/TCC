def posLetra(string, letra, ocorrencia):
    posicao = string.find(letra)
    while posicao >= 0 and ocorrencia > 1:
        posicao = string.find(letra, posicao + 1)
        ocorrencia -= 1
    return posicao