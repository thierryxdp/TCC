def pontos_por_time(j):
    r = {}
    j1 = j[0]
    j2 = j[1]
    t1 = j1[0]
    t2 = j1[1]
    gols = j1[2]
    # jogo 1
    gt1 = gols[0]
    gt2 = gols[1]
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
    gols = j2[2]
    gt1 = gols[1]
    gt2 = gols[0]
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