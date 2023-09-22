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
    for corredor in range(nlin):
        melhor = (corredor, matriz[corredor][volta], volta)
        for volta in range(ncol):
            if matriz[corredor][volta] < melhor[tempo]:
                tupla = (i+1,matriz[i][j],j+1) #de quem, tempo, qual volta

    return tupla