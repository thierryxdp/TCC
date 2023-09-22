def posLetra(string,letra,ocorrencia):
    string = list(string)
    posicao = []
    i = 0 
    while i < len(string):
        if string[i] == letra:
            posicao.append(i)
            i += 1
        i += 1
    if posicao <= (len(ocorrencias)):
        posicao_1 = posicao-1
        return posicao_1[posicao]
    else:
        return -1