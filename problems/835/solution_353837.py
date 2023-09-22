def melhor_volta(matriz_tempo):
    '''Função que recebe uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta, e retorna uma tupla informando de quem foi a melhor volta, qual tempo e em que volta.
    list -> tuple'''
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz_tempo[i][j] < tupla[1]:
                tupla = (i+1,matriz_tempo[i][j],j+1)
    return tupla