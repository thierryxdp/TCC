def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    nlin = 6
    ncol = 10
    corredor = range(6)
    volta = range (10)
    for i in range(nlin):
        for j in range(ncol):
            tempo = matriz[i].index(j)
            melhor = (i, tempo , j)
            if matriz[corredor][volta] < melhor[tempo]:
                tupla = (i+1,matriz[i][j],j+1) #de quem, tempo, qual volta

    return tupla