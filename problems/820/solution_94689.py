def posLetra(texto,letra,num_ocorrencia):
    indice=0
    posicao=0
    while indice < num_ocorrencia:
        if texto.count(letra)<num_ocorrencia:
            return -1
        if texto[indice] == letra:
            posicao=indice
        indice+=1
    return posicao