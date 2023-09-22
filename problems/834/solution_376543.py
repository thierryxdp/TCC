def media_matriz(matriz):
    ''' Calcula a media de todos os numeros de determinada Matriz'''
    lista = 0
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista = matriz[i][j] + lista
        	acumulador = acumulador + 1
    return round(lista/acumulador,2)