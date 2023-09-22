def pontos_por_time(lista):
    jogo1 = lista[0]
    gols1 = jogo1[2]
    jogo2 = lista[1]
    gols2 = jogo2[2]
    time1 = jogo1[0]
    time2 = jogo1[1]
    if gols1[0] > gols1[1] and gols2[1]>gols2[0]:
        return {time1:6,time2:0}
    elif (gols1[0] > gols1[1] and gols2[1]<gols2[0]) or (gols1[0] < gols1[1] and gols2[1]>gols2[0]):
        return {time1:3,time2:3}
    elif gols1[0] == gols1[1] and gols2[1] == gols2[0]:
        return {time1:2,time2:2}
    elif (gols1[0] == gols1[1] and gols2[1]>gols2[0]) or (gols1[0]>gols1[1] and gols2[1]==gols2[0]):
        return {time1:4,time2:1}
    elif (gols1[0] == gols1[1] and gols2[1]<gols2[0]) or (gols1[0]<gols1[1] and gols2[1]==gols2[0]):
        return {time1:1,time2:4}
    else:
        return {time1:0,time2:6}