def melhor_volta(matriz):
    '''funcao que retorna qual corredor
    teve a melhor volta, com o melhor tempo
    entrada: lista
    saida: tupla
    '''
    ranking= []
    i=0
    for corredor in range(6):
        menor_tempo= min(matriz[corredor])
        volta= list.index(matriz[corredor], menor_tempo)
        list.append(ranking,[(corredor+1), menor_tempo, (volta+1)])    
    while i<len(ranking):
        if ranking[i][1]<ranking[i+1][1]:
            return ranking[i]
        i= i+1