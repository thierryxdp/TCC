def pontos_por_time(chaveamento):
    jogo1 = chaveamento[0]
    jogo2 = chaveamento[1]
    time1 = jogo1[0] 
    time2 = jogo1[1] 
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    pontos1 = 0
    pontos2 = 0
    
    if placar1[0] > placar1[1]:
        pontos1 += 3
    if placar2[0] < placar2[1]:
        pontos1 += 3
    if placar1[0] < placar1[1]:
        pontos2 += 3
    if placar2[0] > placar2[1]:
        pontos2 += 3
    if placar1[0] == placar1[1]:
        pontos1 += 1
        pontos2 += 1
    if placar2[0] == placar2[1]:
        pontos1 += 1
        pontos2 += 1
    return {time1 : pontos1 ,time2 : pontos2}