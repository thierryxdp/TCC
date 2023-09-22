def pontos_por_time(x):
# cada jogo
    j1 = x[0]
    j2 = x[1]
# nome dos times para o primeiro jogo
    t1 = j1[0]
    t2 = j1[1]
# gols no primeiro jogo
    gols = j1[2]
    gols_t1 = gols[0]
    gols_t2 = gols[1]
#pontos
    pt_t1 = 0
    pt_t2 = 0
    if gols_t1 > gols_t2:
        pt_t1 += 3
    elif gols_t1 < gols_t2:
        pt_t2 += 3
    else:
        pt_t1 += 1
        pt_t2 += 1
#retorno
    d = {}
    d[t1] = pt_t1
    d[t2] = pt_t2
    return d
#para o segundo jogi
    t1 = j2[0]
    t2 = j2[2]