def pontos_por_time(j):
    r = {}
    j1 = j[0]
    j2 = j[1]
    t1 = j1[0] = j2[1]
    t2 = j1[1] = j2[0]
    gols1 = j1[2]
    gols2 = j2[2]
    i1 = gols1[0]
    i2 = gols1[1]
    v1 = gols2[1]
    v2 = gols2[0]
    # jogo ida
    if i1 == i2:
        r[t1] = 1
        r[t2] = 1
    if i1 > i2:
        r[t1] = 3
        r[t2] = 0
    if i1 < i2:
        r[t1] = 0
        r[t2] = 3
    # jogo volta
    if v1 == v2:
        r[t1] = r[t1] + 1
        r[t2] = r[t2] + 1
    if v1 > v2:
        r[t1] = r[t1] + 3
        r[t2] = r[t2]
    if v1 < v2:
        r[t1] = r[t1]
        r[t2] = r[t2] + 3
        return r