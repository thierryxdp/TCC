def media_matriz(matriz):
    "Função que dada uma matriz calcula a média de todos seus números. list --> float"
    soma=0
    div=len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma=soma+j
    media=soma/div
    return round(media,2)