def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    melhor = min(matriz)
    corredor = matriz.index(melhor) + 1
    menor_tempo = min(melhor)
    melhor_volta = matriz.index(menor_tempo) + 1
    
    return (corredor, menor_tempo, melhor_volta)