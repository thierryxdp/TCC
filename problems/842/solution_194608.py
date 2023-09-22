def pontos_por_time(j):
    r = {}
    j1 = j[0]
    j2 = j[1]
    t1 = j1[0] = j2[1]
    t2 = j1[1] = j2[0]
    gols1 = j1[2]
    gols2 = j2[2]
    gt1 = gols1[0]
    gt2 = gols1[1]
    # jogo 1
    if gt1 == gt2:
        r[t1] = 1
        r[t2] = 1
    if gt1 > gt2:
        r[t1] = 3
        r[t2] = 0
    if gt1 < gt2:
        r[t1] = 0
        r[t2] = 3
    # jogo 2
    if gt1 == gt2:
        r[t1] = r[t1] + 1
        r[t2] = r[t2] + 1
    if gt1 > gt2:
        r[t1] = r[t1] + 3
        r[t2] = r[t2] + 0
    if gt1 < gt2:
        r[t1] = r[t1] + 0
        r[t2] = r[t2] + 3
        return r