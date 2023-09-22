def pontos_por_time(lista):
    timepontos = dict()
    partida1 = lista[0]
    partida2 = lista[1]
    time1 = partida1[0]
    time2 = partida2[0]
    golsp1 = partida1[2]
    golsp2 = partida2[2]
    pontos_t1 = []
    pontos_t2 = []
    timepontos[time1] = pontos_t1
    timepontos[time2] = pontos_t2
    if golsp1[0] > golsp1[1]:
        pontos_t1 += '3'
    if golsp1[0] < golsp1[1]:
        pontos_t2 += '3'
    if golsp1[0] == golsp1[1]:
        pontos_t1 += '1'
        pontos_t2 += '1'
    return timepontos