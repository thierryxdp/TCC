def posLetra(frase, letra, ocorrencia):
    posicao = 0
    if ocorrencia > str.count(frase,letra):
        return -1
    while