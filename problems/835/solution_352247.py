def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com os
    tempos em segundos dos corredores 
    em cada volta, retorna uma tupla informando
    de quem foi a melhor volta da prova e o melhor
    tempo.
    list -> tup'''
    tup = ()
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < 0:
                tup += (i,matriz[i][j],j)
    return tup