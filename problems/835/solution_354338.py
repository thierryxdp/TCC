def melhor_volta(matriz):
    '''função em dada uma matriz com os tempos das corredores
    em cada volta e retorna uma tupla contendo quem teve a 
    melhor volta, em que tempo e em que volta;
    int -> int'''
    menor = 0
    for volta in range(0, len(matriz)):
        for tempo in range(0, len(matriz[volta])):
            if min(matriz[volta][tempo], menor)  matriz[volta][tempo]:
                menor - min(matriz[volta][tempo], menor)
                ganhador - volta + 1
                v - tempo + 1
    return ganhador, menor, v