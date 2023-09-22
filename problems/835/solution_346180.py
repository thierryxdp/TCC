def melhor_volta(matriz):
    '''Retorna uma tupla informando de quem foi a melhor volta, em quanto tempo e em que volta de acordo com os valores da matriz de entrada(6X10);
    list(list) -> tup'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == 9:
                if matriz[i][j] < matriz[i][j-1]:
                    tupla = (i+1, matriz[i][j], j+1)
            else:
                j = j+1
                if matriz[i][j] < matriz[i][j-1]:
                    tupla = (i+1, matriz[i][j], j+1)
    return tupla