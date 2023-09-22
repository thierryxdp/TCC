def pontos_por_time(partidas):
    '''função dado dois resultados de jogos calcula quantidade de pontos e retorna.
    lista -> dicionario'''
    jogo1 = partidas[0]
    jogo2 = partidas[1]
    time2 = jogo2[0]
    time1 = jogo2[1]
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    pontos_time1 = 0
    pontos_time2 = 0
    if placar1[0] > placar1[1]:
        pontos_time1 += 3
    if placar1[0] < placar1[1]:
        pontos_time2 += 3
    if placar1[0] == placar1[1]:
        pontos_time1 += 1
        pontos_time2 += 1
    if placar2[0] > placar2[1]:
        pontos_time2 += 3
    if placar2[0] < placar2[1]:
        pontos_time1 += 3
    if placar2[0] == placar2[1]:
        pontos_time1 += 1
        pontos_time2 += 1
    if pontos_time1 > pontos_time2:
        return {time1:pontos_time1, time2:pontos_time2}
    else:
        return {time1:pontos_time1, time2:pontos_time2}