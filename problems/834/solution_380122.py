def media_matriz(matriz):
    '''Essa funcao retorna a media aritimética de todos os
    valores contidos dentro de uma matriz 
    list->int'''
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            	total=total+matriz[i][j]
    return round((total)/(len(matriz[0])*len(matriz)),2)