def melhor_volta(matriz):
    '''dada uma matriz(matriz) 6 x 10 com os tempos dos corredores em cada volta,
    retorna uma tupla informando de quem foi a melhor volta, com qual tempo e em que volta;
    list -> tuple(str, float, int)'''
    melhor_v = matriz[0][0]
    piloto = 0
    volta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < melhor_v:
                melhor_v = matriz[i][j]
                piloto = i + 1
                volta = j + 1
    return (piloto, melhor_v, volta)