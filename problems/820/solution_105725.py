def posLetra(string,letra,ocorrencia):
    string = list(string)
    posicao = []
    i = 0 
    while i < len(string):
        if string[i] == letra:
            posicao.append(i)
            i += 1
        i += 1
    if ocorrencia <= (len(posicao)):
        ocorrencia_1 = ocorrencia-1
        return posicao[ocorrencia_1]
    else:
        return -1