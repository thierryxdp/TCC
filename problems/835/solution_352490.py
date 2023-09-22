def melhor_volta(matriz):
    '''Função que recebe uma matriz com o tempo em segundos
    dos corredores em cada volta, e retorna uma tupla com
    quem foi a melhor volta, com qual tempo e em que volta.
    list -> tuple
    '''
    Tempo = []
    Volta = []
    V = []

    for voltas in range(6):
        Tempo += [(voltas+1,min(matriz[voltas]),matriz[voltas].index(min(matriz[voltas])))]
        V += [min(matriz[voltas])]
    v = V.index(min(V))
    
    return Tempo[v]