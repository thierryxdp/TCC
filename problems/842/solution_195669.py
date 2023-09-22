def pontos_por_time(lll):
    pontotime0 = 0
    pontotime1 = 0
    times = lll[0]
    gols = lll[1]
    if gols[0] > gols[1]:
        pontotime0 + 3
    if gols[1] > gols[0]:
        pontotime1 + 3
    if gols[1] = gols[0]:
        pontotime1 + 1
        pontotime0 + 1
    return [pontotime0, pontotime1]