def media_matriz(matriz):
    '''funcao que, dada uma matriz de inteiros nao vazia, retorna a media de todos os numeros dela;
    list -> float'''
    soma=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            soma=soma+matriz[i][j]
    return soma/(len(matriz)8len(matriz[0]))