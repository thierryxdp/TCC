def melhor_volta(x):
    '''Dada uma matriz 6x10 com os tempos, em segundos, dos corredores em cada volta, retorna de quem foi a melhor volta, com qual tempo e em qual volta.
    list -> tuple'''
    for i in range(len(x)):
        for j in range(len(x[i])):