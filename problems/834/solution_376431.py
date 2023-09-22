def media_matriz(matriz):
    """retorna a media dos elementos de uma matriz com duas  asas decimais de precisão
    list(list)->float"""
    a=[]
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            a+=[matriz[i][j]]
    return soma/len(a)