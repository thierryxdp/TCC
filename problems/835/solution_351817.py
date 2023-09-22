def melhor_volta (matriz):
    '''função que dada uma matriz 6x10 com os tempos em s dos
       corredores em cada volta de Kart, retorna uma tupla que
       indica quem foi o melhor, com qual tempo e em que volta.
       : list -> tuple
    '''
    corredores = 6
    voltas = 10
    menores = []
    menor_volta = []
    
    for i in range(corredores):
        for j in range(voltas):
            if matriz[i][j] == min(matriz[i]):
                menores.append(matriz[i][j])
                menor_volta.append(j+1)
    menor_tempo = min(menores)
    corredor = menores.index(menor_tempo) 
    volta = menor_volta[corredor]
    
    return corredor + 1, menor_tempo, volta