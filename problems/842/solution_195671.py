def pontos_por_time(lll):
    time0 = 0
    time1 = 0
    times = lll[0]
    gols = lll[1]
    if gols[0] > gols[1]:
        ponto0 = time0 + 3
    if gols[1] > gols[0]:
        ponto1 = time1 + 3
    if gols[1] == gols[0]:
        ponto1 = time1 + 1
        ponto0 = time0 + 1
    return [ponto0, ponto1]