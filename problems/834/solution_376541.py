def media_matriz(matriz):
    lista = 0
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista = matriz[i][j] + lista
        	acumulador = acumulador + 1
    return lista/acumulador