def melhor_volta(matriz):
    '''
       funcao que recebe como entrada uma matriz 6 x 10 com 
       os tempos em segundos dos corredores em cada volta e 
       retorna uma tupla informando qual corredor fez a 
       melhor volta, com qual tempo e em qual volta
       list -> tuple 
    '''
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    minimo = []
    for i in range(nlinhas):
        for j in range(ncolunas):
            minimo.append(matriz[i][j])
            if matriz[i][j] == min(minimo):
                corredor = i + 1
                volta = j + 1
                resultado = matriz[i][j]
    return (corredor,resultado,volta)