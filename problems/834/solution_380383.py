def media_matriz(matriz):
    '''funcao que dado como entrada uma matriz de inteiros nao vazia retorna a media dos numeros dessa matriz
    list->float'''
    soma=0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            soma=soma+matriz[x][y]
    media=soma/len(matriz)+len(matriz[0])
    return media