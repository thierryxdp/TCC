def pontos_por_time(lista):
    jogo1 = lista[0]
    jogo2 = lista[1]
    times1 = jogo1[0]
    times2 = jogo2[0]
    gols1 = jogo1[1]
    gols2 = jogo2[1]
    dic = {times1[0]: 0, times1[1]: 0}
    if gols1[0] > gols1[1]:
        if gols2[0] > gols2[1]:
            dic[times1[0]] = 6
        if gols2[0] == gols2[1]:
            dic[times1[0]] = 4
            dic[times1[1]] = 1
        if gols2[0] < gols2[1]:
            dic[times1[0]] = 3
            dic[times1[1]] = 3
    if gols1[0] == gols1[1]:
        if gols2[0] > gols2[1]:
            dic[times1[0]] = 4
            dic[times1[1]] = 1
        if gols2[0] == gols2[1]:
            dic[times1[0]] = 2
            dic[times1[1]] = 2
        if gols2[0] < gols2[1]:
            dic[times1[0]] = 1
            dic[times1[1]] = 4
    if gols1[0] < gols1[1]:
         if gols2[0] > gols2[1]:
            dic[times1[0]] = 3
            dic[times1[1]] = 3
        if gols2[0] = gols2[1]:
            dic[times1[0]] = 1
            dic[times1[1]] = 4
        if gols2[0] < gols2[1]:
            dic[times1[1]] = 6
    return dic