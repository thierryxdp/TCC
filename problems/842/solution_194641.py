def pontos_por_time(ls):
    d = {}
    j1 = ls[0] #jogo 1 
    j2 = ls[1] #jogo 2
    t1 = j1[0]
    t2 = j1[1]
    gols = j1[2]
    # primeiro jogo
    t1_gols = gols[0]
    t2_gols = gols[1]
    if t1_gols == t2_gols:
        d[t1] = 1
        d[t2] = 1
    if t1_gols > t2_gols:
        d[t1] = 3
        d[t2] = 0
    if t1_gols < t2_gols:
        d[t1] = 0
        d[t2] = 3
    # segundo jogo
    gols = j2[2]
    t2_gols = gols[0]
    t1_gols = gols[1]
    if t1_gols == t2_gols:
        d[t1] = d[t1] + 1
        d[t2] = d[t2] + 1
    if t1_gols > t2_gols:
        d[t1] = d[t1] + 3
        d[t2] = d[t2] + 0
    if t1_gols < t2_gols:
        d[t1] = d[t1] + 0
        d[t2] = d[t2] + 3
    return d