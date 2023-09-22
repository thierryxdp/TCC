def media_matriz(matriz):
    soma=0
    for linha in matriz:
        soma+=sum(linha)
        media=soma/len(linha)+len(matriz[linha])
    return soma