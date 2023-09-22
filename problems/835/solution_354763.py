def melhor_volta(matriz):
    '''Recebe uma matrix 6x10 com os tempos dos corredores
    em cada volta e retorna, numa tupla, quem foi a melhor
    volta, com qual tempo e em qual volta'''
    '''list->tuple'''
    menor=volta=vencedor=1000
    for v in range(0,len(matriz)):
        for t in range(0,len(matriz[v])):
            if min(matriz[v][t],menor==matriz[v][t]
                   menor=min(matriz[v][t],menor)
                   vencedor=v+1
                   volta=t+1
   return vencedor, menor, volta