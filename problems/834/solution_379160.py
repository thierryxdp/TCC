def media_matriz(matriz):
    
# A função recebe uma matriz de inteiros não vazia e retorna a média de todos os números da    
# matriz, com exatamente duas casas decimais.
# list->float

    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                       soma=soma+matriz[i][j]
        media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)