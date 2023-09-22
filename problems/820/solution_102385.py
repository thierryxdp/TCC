def posLetra(frase, letra, ocorrencia):
    posicao = 0
    if ocorrencia > str.count(frase,letra):
        return -1
    while ocorrencia>0:
        posicao=str.find(frase,letra,posicao)
        posicao=posicao+1
        ocorrencia=ocorrencia-1
    return posicao-1