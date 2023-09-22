def melhor_volta(matriz_tempos):
    '''função que dada uma matriz 6x10 com os tempos em segundos de corredores em cada volta, 
    retona uma tupla com quem fez a melhor volta, o tempo e em qual volta
    list'''
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempos[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempos[i][j],j+1)
    return tupla