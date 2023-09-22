def melhor_volta(matriz):
    '''Função que recebe uma matriz com o tempo em segundos
    dos corredores em cada volta, e retorna uma tupla com de
    quem foi a melhor volta, com qual tempo e em qual volta.
    list -> tuple
    '''
    Tempo = []
    Volta = []
    for voltas in range(6):
        for tempo in range(10):
            if matriz[voltas][tempo] == min(matriz[voltas]):
                Tempo.append(tempo)
    V = Tempo.index(min(Volta))
    T = min(Volta)
    corredores = matriz[V].index(T) + 1        
    return (V + 1,T,corredores)