def melhor_volta(matriz):
    '''Retorna uma tupla informando de quem foi a melhor volta, em quanto tempo e em que volta de acordo com os valores da matriz de entrada(6X10);
    list(list) -> tup'''
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0][0])):
            if matriz[0][i][j] < matriz[0][i][j-1]:
                tupla = (i+1, matriz[0][i][j], j+1)

    return tupla