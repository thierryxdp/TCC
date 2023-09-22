def posLetra(texto,letra,num_ocorrencia):
    indice=0
    posicao=0
    while indice < num_ocorrencia:
        if letra not in texto[0:num_ocorrencia]:
            return -1
        if texto[indice] == letra:
            posicao=indice
    return posicao