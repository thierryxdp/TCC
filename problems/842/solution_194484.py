def pontos_por_time(jogo1,jogo2):
    time1 = jogo1[0] 
    time2 = jogo1[1] 
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    tabela = {time1 : x ,time2 : y}
    x = 0
    y = 0
    if placar1[0] > placar1[1]:
        x += 3
    if placar2[0] < placar2[1]:
        x += 3
    if placar1[0] < placar2[1]:
        y += 3
    if placar2[0] > placar2[1]:
        y += 3
    if placar1[0] == placar1[1]:
        x += 1
        y += 1
    if placar2[0] == placar2[1]:
        x += 1
        y += 1
    return tabela