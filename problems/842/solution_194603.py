def pontos_por_time(j):
    r = {}                  # r = resultado
    j = [j1,j2]             # j = jogos
    j1 = [time1,time2,gols_j1]
    gols_j1 = [i1,i2]
    j2 = [time2,time1,gols_j2]
    gols_j2 = [v1,v2]
    r_t1 = i1 + v1
    r_t2 = i2 + v2
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