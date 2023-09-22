def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    corredores = len(matriz)
    voltas = len(matriz[0])
    melhores = []
    for corredor in range(corredores):
        melhor = ()
        for tempo in matriz[corredor]:
            if tempo == min(matriz[corredor]):
                volta = matriz[corredor].index(tempo) + 1
                melhor += corredor + 1, tempo, volta
                melhores += melhor
    menor_tempo = min(melhores)
            
     
         #   melhor_volta = list.index(corredor,menor_tempo) + 1
    #return (corredor+1, menor_tempo, melhor_volta)
    return melhores