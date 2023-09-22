def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    tupla = (0,float('inf'),0)

    for i in range(6):

    for j in range(10):

        if matriz_tempos[i][j] < tupla[1]:

            tupla = (i+1,matriz_tempos[i][j],j+1) #de quem, tempo, qual volta

    return tupla