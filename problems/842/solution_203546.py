def pontos_por_time(l):
    time1 = l[0][0]
    time2 = l[0][1]

    gtime1_jogo1 = l[0][2][0]
    gtime2_jogo1 = l[0][2][1]
    gtime1_jogo2 = l[1][2][1]
    gtime2_jogo2 = l[1][2][0]

    ptime1_jogo1 = 0
    ptime2_jogo1 = 0

    if gtime1_jogo1 > gtime2_jogo1:
        ptime1_jogo1 = ptime1_jogo1 + 3
    if gtime1_jogo1 < gtime2_jogo1:
        ptime2_jogo1 = ptime2_jogo1 +3
    if gtime1_jogo1 == gtime2_jogo1:
        ptime1_jogo1 = ptime1_jogo1 + 1
        ptime2_jogo1 = ptime2_jogo1 + 1

    ptime1_jogo2 = 0
    ptime2_jogo2 = 0

    if gtime1_jogo2 > gtime2_jogo2:
        ptime1_jogo2 = ptime1_jogo2 + 3
    if gtime1_jogo2 < gtime2_jogo2:
        ptime2_jogo = ptime2_jogo2 + 3
    if gtime1_jogo2 == gtime2_jogo2:
        ptime1_jogo2 = ptime1_jogo2 + 1
        ptime2_jogo2 = ptime2_jogo2 + 1

    ptime1 = ptime1_jogo1 + ptime1_jogo2
    ptime2 = ptime2_jogo1 + ptime2_jogo2
    tabela = {time1:ptime1, time2:ptime2}

    return tabela