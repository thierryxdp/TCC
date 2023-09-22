def pontos_por_time(listas):
    """
    Essa função ira retornar o time vencedor depois de duas rodadas
    os times serao dados em uma lista com 2 elementos sendo eles tambem uma lista
    list->dict
    """
    
    dicionario = {}
    pontos_time1 = 0
    pontos_time2 = 0
    jogo1=listas[0]
    jogo2=listas[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    
    time1=jogo1[0]
    time2=jogo1[1]
    
    if placar1[0] > placar1[1] and placar2[1] > placar2[0]:
        pontos_time1 = 6
        pontos_time2 =0
    elif placar1[0] < placar1[1] and placar2[1] < placar2[0]:
        pontos_time2 = 6
        pontos_time1 = 0
        
    elif placar1[0] > placar1[1] and placar2[1] < placar2[0] or placar1[0] < placar1[1] and placar2[1] > placar2[0]:
        pontos_time1 = 3
        pontos_time2 = 3
    elif placar1[0] < placar1[1] and placar2[1] > placar2[0] or placar1[0] > placar1[1] and placar2[1] < placar2[0]:
        pontos_time2 = 3
        pontos_time1 = 3
    
    elif placar1[0] == placar1[1] and placar2[1] == placar2[0]:
        pontos_time2 = 2
        pontos_time1 = 2
        
    elif placar1[0] > placar1[1] and placar2[1] == placar2[0] or placar1[0] == placar1[1] and placar2[1] > placar2[0]:
        pontos_time1 = 4
        pontos_time2 = 1
    elif placar1[0] < placar1[1] and placar2[1] == placar2[0] or placar1[0] == placar1[1] and placar2[1] < placar2[0]:
        pontos_time1 = 1
        pontos_time2 = 4    
     
    
    dicionario[time1] = pontos_time1
    dicionario[time2] = pontos_time2
    
    return dicionario