def pontos_por_time(chaveamento):
    jogo1 = chaveamento[0]
    jogo2 = chaveamento[1]
    time1 = jogo1[0] 
    time2 = jogo1[1] 
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    x = 0
    y = 0
    
    if placar1[0] > placar1[1]:
        x += 3
    if placar2[0] < placar2[1]:
        x += 3
    if placar1[0] < placar1[1]:
        y += 3
    if placar2[0] > placar2[1]:
        y += 3
    if placar1[0] == placar1[1]:
        x += 1
        y += 1
    if placar2[0] == placar2[1]:
        x += 1
        y += 1
    if x > y:
        return { time1 : x , time2 : y }
    if x < y:
        return { time2 : y , time1 : x }