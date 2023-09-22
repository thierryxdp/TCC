def posLetra(frase,letra,n):
    posicao = 0
    ocorrencia = 0
    proximo = 0
    while ocorrencia < n:
        posicao = str.find(frase, letra, proximo)
        proximo = posicao + 1
        ocorrencia = ocorrencia + 1
    return posicao