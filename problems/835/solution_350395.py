def melhor_volta(matriz):
    '''funcao que retorna qual corredor
    teve a melhor volta, com o melhor tempo
    entrada: lista
    saida: tupla
    '''
    ranking= []
    i=1
    for corredor in range(6):
        menor_tempo= min(matriz[corredor])
        volta= list.index(matriz[corredor], menor_tempo)
        list.append(ranking,[(corredor+1), menor_tempo, (volta+1)])    
    if ranking[0][1]<ranking[1][1]:
        return tuple(ranking[0])
    if ranking[1][1]<ranking[2][1]:
        return tuple(ranking[1])
    if ranking[2][1]<ranking[3][1]:
        return tuple(ranking[2])
    if ranking[3][1]<ranking[4][1]:
        return tuple(ranking[3])
    if ranking[4][1]<ranking[5][1]:
        return tuple(ranking[4])
    if ranking[5][1]<ranking[0][1]:
        return tuple(ranking[5])