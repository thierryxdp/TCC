def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com os
    tempos em segundos dos corredores 
    em cada volta, retorna uma tupla informando
    de quem foi a melhor volta da prova e o melhor
    tempo.
    list -> tup'''
    tup = ()
    m = []
    for i in range(6):
        m += [min(matriz[i])]
        for j in range(10):
            if matriz[i][j] == min(m) :
                tup +=(i+1,matriz[i][j],j+1)
    return tup