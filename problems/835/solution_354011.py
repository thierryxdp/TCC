def melhor_volta(matriz):
    '''Função que, dada uma matriz com os tempos em segundos dos
    corredores em cada volta, retorna de quem foi a melhor volta,
    com qual tempo e em que volta foi esse evento
    list -> tuple'''
    tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla