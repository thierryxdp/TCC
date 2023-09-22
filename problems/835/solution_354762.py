def melhor_volta(matriz):
    '''Recebe uma matrix 6x10 com os tempos dos corredores
    em cada volta e retorna, numa tupla, quem foi a melhor
    volta, com qual tempo e em qual volta'''
    '''list->tuple'''
    menor=volta=vencedor=1000
    for v in range(0,len(matriz)):
        for tempo in range(0,len(matriz[v])):
            if min(matriz[v][tempo],menor==matriz[v][tempo]
                          menor=min(matriz[v][tempo],menor)
                                           vencedor=v+1
                                           volta=tempo+1
    return vencedor, menor, volta