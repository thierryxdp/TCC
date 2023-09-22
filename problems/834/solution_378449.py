def media_matriz(matriz):
    """ Função que dada uma matriz, retorna a média dee todos os seus números 
    list -> float """
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+matriz[i][j]
    a=len(matriz)*len(matriz[0])
    return round(soma/a,2)