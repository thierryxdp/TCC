def pontos_por_time(lista):
    '''Função que recebe uma lista com uma série de dois jogos entre dois times, e
    retorna a pontuação final dos dois em um dicionário
    lista -> dicionário'''
    jogo1 = lista[0]
    jogo2 = lista[1]
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    if placar1[0] > placar1[1]:
        time1 = 3
    	time2 = 0
    elif placar1[0] < placar1[1]:
        time1 = 0
        time2 = 3
    else:
        time1 = 1
        time2 = 1
    if placar2[0] < placar2[1]:
        time1 += 3
    	time2 += 0
    elif placar2[0] > placar2[1]:
        time1 += 0
        time2 += 3
    else:
        time1 += 1
        time2 += 1
    dicionario = {jogo1[0] : time1,  jogo2[0] : time2}
    return dicionario