def pontos_por_time(lista):
    a1 = lista[0]
    a2 = lista[1]
    time1 = a1[0]
    time2 = a1[1]
    placar1 = a1[2]
    placar2 = a2[2]
    
    if (placar1[0] > placar1[1]) and (placar2[0] < placar2[1]):
        ptstime1 = 6
        ptstime2 = 0
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] > placar1[1]) and (placar2[0] > placar2[1]):
        ptstime1 = 3
        ptstime2 = 3
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] < placar1[1]) and (placar2[0] < placar2[1]):
        ptstime1 = 3
        ptstime2 = 3
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] > placar1[1]) and (placar2[0] == placar2[1]):
        ptstime1 = 4
        ptstime2 = 1
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] == placar1[1]) and (placar2[0] < placar2[1]):
        ptstime1 = 4
        ptstime2 = 1
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] == placar1[1]) and (placar2[0] == placar2[1]):
        ptstime1 = 2
        ptstime2 = 2
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] == placar1[1]) and (placar2[0] > placar2[1]):
        ptstime1 = 1
        ptstime2 = 4
        return {time1:ptstime1,time2:ptstime2}
    elif (placar1[0] < placar1[1]) and (placar2[0] == placar2[1]):
        ptstime1 = 1
        ptstime2 = 4
        return {time1:ptstime1,time2:ptstime2}
    else:
        ptstime1 = 0
        ptstime2 = 6
        return {time1:ptstime1,time2:ptstime2}