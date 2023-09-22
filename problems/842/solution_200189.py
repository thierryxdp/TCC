def pontos_por_time(gols):
    gols_ida = gols[0]
    gols_volta = gols[1]
    if gols_ida[2][0] > gols_ida[2][1]:
        pontos_time1 = 3
        pontos_time2 = 0
    elif gols_ida[2][0] == gols_ida[2][1]:
        pontos_time1 = 1
        pontos_time2 = 1
    elif gols_ida[2][0] < gols_ida[2][1]:
        pontos_time1 = 0
        pontos_time2 = 3
    if gols_volta[2][1] > gols_volta[2][0]:
        pontos_time1 += 3
    elif gols_volta[2][1] == gols_volta[2][0]:
        pontos_time1 += 1
        pontos_time2 += 1
    elif gols_volta[2][1] < gols_volta[2][0]:
        pontos_time2 += 3
    return {gols[0][0]: pontos_time1, gols[0][1]: pontos_time2}