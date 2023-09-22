def pontos_por_time(lista):
    timepontos = {time1, pontos_t1, time2, pontos_t2}
    partida1 = lista[0]
    partida2 = lista[1]
    time1 = partida1[0]
    time2 = partida2[0]
    golsp1 = partida1[2]
    golps2 = partida2[2]
    if golsp1[0] > golsp1[1]:
        pontos_t1 += 3
    if golsp1[0] < golsp1[1]:
        pontos_t2 += 3
    if goslp1[0] == golsp1[1]:
        pontos_t1 += 1
        pontos_t2 += 1
    return timepontos