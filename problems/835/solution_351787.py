def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    
    corredores = 6
    voltas = 10
    melhores = ()
    for corredor in range(corredores):
        melhor = ()
        for tempo in matriz[corredor]:
            if tempo == min(matriz[corredor]):
                volta = matriz[corredor].index(tempo) + 1
                melhor += corredor + 1, tempo, volta
                melhores += melhor
    menor_tempo = min(melhores)
    return melhor