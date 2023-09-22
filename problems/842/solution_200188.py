def pontos_por_time(gols):
    gols_ida = gols[0]
    gols_volta = gols[1]
    if gols_ida[2][0] > gols_ida[2][1]:
        pontos_cormengo = 3
        pontos_flaminthias = 0
    elif gols_ida[2][0] == gols_ida[2][1]:
        pontos_cormengo = 1
        pontos_flaminthias = 1
    elif gols_ida[2][0] < gols_ida[2][1]:
        pontos_cormengo = 0
        pontos_flaminthias = 3
    if gols_volta[2][1] > gols_volta[2][0]:
        pontos_cormengo += 3
    elif gols_volta[2][1] == gols_volta[2][0]:
        pontos_cormengo += 1
        pontos_flaminthias += 1
    elif gols_volta[2][1] < gols_volta[2][0]:
        pontos_flaminthias += 3
    return {'Cormengo': pontos_cormengo, 'Flamínthias': pontos_flaminthias}