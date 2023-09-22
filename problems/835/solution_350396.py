def melhor_volta(matriz):
    '''funcao que retorna qual corredor
    teve a melhor volta, com o melhor tempo
    entrada: lista
    saida: tupla
    '''
    ranking= []
    auxiliar= []
    i= 0
    for corredor in range(6):
        menor_tempo= min(matriz[corredor])
        volta= list.index(matriz[corredor], menor_tempo)
        list.append(ranking,[(corredor+1), menor_tempo, (volta+1)])    
    for a in range(6)
        the_flash= min(ranking[a][1])
        list.append(auxiliar, the_flash)
        
    n= min(axuiliar)
    c= list.index(ranking, n)
    return tuple(ranking[c])