def pontos_por_time(jogos):
    jogos = [jogo1,jogo2]
    jogo1 = [time1,time2,gols1]
    gols1 = [i1,i2]
    jogo2 = [time2,time1,gols2]
    gols2 = [v1,v2]
    resultado_t1 = i1 + v1
    resultdo_t2 = i2 + v2
    r = {}
    if i1 = i2:
        r[i1] = 1
        r[i2] = 1
    if i1 > i2:
        r[i1] = 3
        r[i2] = 0
    if i1 < i2:
        r[i1] = 0
        r[i2] = 3
    if v1 = v2:
        r[v1] = 1
        r[v2] = 1
    if v1 > v2:
        r[v1] = 3
        r[v2] = 0
    if v1 < v2:
        r[v1] = 0
        r[v2] = 3
    return resultado