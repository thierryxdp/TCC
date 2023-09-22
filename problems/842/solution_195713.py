def pontos_por_time(partidas):
    d = {}
    jogo1 = partidas[0]
    jogo2 = partidas[1]
    time1 = jogo1[0]
    time2 = jogo1[1]
    gols = jogo1[2]
    #primeiro jogo
    gols_time1 = gols[0]
    gols_time2 = gols[1]
    if gols_time1 == gols_time2:
        d[time1] = 1
        d[time2] = 1
    if gols_time1 > gols_time2:
        d[time1] = 3
        d[time2] = 0
    if gols_time1 < gols_time2:
        d[time1] = 0
        d[time2] = 3
    #segundo jogo
    gols = jogo2[2]
    gols_time1 = gols[1]
    gols_time2 = gols[0]
    if gols_time1 == gols_time2:
        d[time1] += 1
    if gols_time1 > gols_time2:
        d[time1] += 3
        d[time2] += 0
    if gols_time1 < gols_time2:
        d[time2] += 3
        d[time1] += 0
    return d