def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    melhor = min(matriz[0])
    #for corredor in range(6):
     #if corredor == melhor:
        #      menor_tempo = min(corredor)
         #   melhor_volta = list.index(corredor,menor_tempo) + 1
    #return (corredor+1, menor_tempo, melhor_volta)
    return melhor