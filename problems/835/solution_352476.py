def melhor_volta(matriz):
    '''Função que recebe uma matriz com o tempo em segundos
    dos corredores em cada volta, e retorna uma tupla com de
    quem foi a melhor volta, com qual tempo e em que volta.
    list -> tuple
    L1 = tempo
    L2 = voltas
    '''
    L1 = []
    L2 = []

    for voltas in range(6):
        for tempo in range(10):
            if matriz[voltas][tempo] == min(matriz[voltas]):
                L1.append(tempo)

    for i in range(6):
        L2.append(matriz[i][L1[i]])

    V = L1.index(min(L2))
    T = min(L2)
    corredores = matriz[V].index(T) + 1

    return (V + 1, T, corredores)