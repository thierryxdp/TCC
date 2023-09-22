def posLetra(frase,letra,ocorrencia):
    contagem = str.count(frase,letra)
    posicao=str.index(frase,letra)
    if ocorrencia > contagem:
        return -1
    return posicao