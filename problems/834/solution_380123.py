def media_matriz(matriz):
    '''essa funcao retorna uma media aritmetica de todos os valores
    dentro de uma matriz
    list->float'''
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            	total=total+matriz[i][j]
    return round((total)/(len(matriz[0])*len(matriz)),2)