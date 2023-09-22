def pontos_por_time(lista):
    '''Função que recebe uma lista com uma série de dois jogos entre Cormengo e Flamínthians, e
    retorna a pontuação final dos dois em um dicionário
    lista -> dicionário'''
    jogo1 = lista[0]
    jogo2 = lista[1]
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    if placar1[0] > placar1[1]:
        cormengo = 3
    	flaminthians = 0
    elif placar1[0] < placar1[1]:
        cormengo = 0
        flaminthinas = 3
    else:
        cormengo = 1
        flaminthians = 1
    if placar2[0] < placar2[1]:
        cormengo += 3
    	flaminthians += 0
    elif placar2[0] > placar2[1]:
        cormengo += 0
        flaminthinas += 3
    else:
        cormengo += 1
        flaminthians += 1
    dicionario = {'Cormengo' : cormengo, 'Flamínthians' : flaminthians}
    return dicionario