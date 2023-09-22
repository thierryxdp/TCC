def melhor_volta(matriz):
    '''Dado uma matrix 6x10, simulando tempos de corredores em voltas, retorna uma tupla,
    informando, de quem foi a volta mais rápida, com qual tempo, e em qual volta.
    list -> tup'''
    melhor=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]<melhor:
                melhor=matriz[i][j]
                melhor_corredor=i
                melhor_volta=j
    return (melhor_corredor+1,melhor,melhor_volta+1)