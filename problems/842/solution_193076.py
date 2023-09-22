def pontos_por_time (x):
    time1 = times[0]
    time2 = times[1]
    pontos = [ponto1,ponto2]
    pontos[0] = ponto1
    pontos[1] = ponto2
    times = [time1,time2]
    x = [ times , pontos ]

    if pontos[0] > pontos[1]:
        p1 = +3
    elif pontos[0] < pontos[1]:
        p2 = +3
    else:
        p1 = +1
        p2 + 1
    return {times[0]:p1, times[1]:p2}