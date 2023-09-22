def melhor_volta(matriz):
    '''Função que recebe uma matriz com os tempos dos corredores de uma corrida,
    e retorna uma tupla informando a melhor volta,tempo e em qual volta.
    list->tuple'''
    melhor=[-1,999999, -1]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j]< melhor[1]:            
                melhor[0] = i
                melhor[1] = matriz[i][j]
                melhor[2] = j
    return tuple(melhor)