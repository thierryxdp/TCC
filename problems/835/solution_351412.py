def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    corredores = len(matriz)
    voltas = len(matriz[0])
    
    for corredor in range(corredores):
        for tempo in range(voltas):
            if matriz[corredor][tempo] == min(matriz[corredor]):
                volta = matriz[corredor].index(matriz[corredor][tempo]) + 1
                #melhor += corredor + 1, tempo, volta
                #melhores += melhor
    #menor_tempo = min(melhores)
    return volta