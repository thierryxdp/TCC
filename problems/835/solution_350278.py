def melhor_volta(matriz):
    '''Dada uma matriz 6x10 com os tempos em segundos dos corredores em
       cada volta, retorna uma tupla contendo: quem fez a melhor volta da prova,
       com qual tempo e em que volta;
       list -> tuple'''
    driver = ''
    best_time = matriz[0][0]
    lap = 0
    for piloto in matriz:
        for volta in piloto:
            if volta < best_time:
                driver = matriz.index(piloto)
                best_time = volta
                lap = piloto.index(volta)
    return (driver + 1, best_time, lap + 1)