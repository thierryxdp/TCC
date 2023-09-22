def pontos_por_time(lista):
    timepontos = dict()
    partida1 = lista[0]
    partida2 = lista[1]
    time1 = partida1[0]
    time2 = partida2[0]
    golsp1 = partida1[2]
    golsp2 = partida2[2]
    timepontos[time1] = 0
    timepontos[time2] = 0
    if golsp1[0] > golsp1[1]:
        timepontos[time1] += 3
    if golsp1[0] < golsp1[1]:
        timepontos[time2] += 3
    if golsp1[0] == golsp1[1]:
        timepontos[time1] += 1
        timepontos[time2] += 1
    if golsp2[0] > golsp2[1]:
        timepontos[time2] += 3
    if golsp2[0] < golsp2[1]:
        timepontos[time1] += 3
    if golsp2[0] < golsp2[1]:
        timepontos[time1] += 1
        timepontos[time2] += 1
        
    return timepontos