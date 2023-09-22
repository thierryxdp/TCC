def pontos_por_time(lista):
    """."""
    jogo1 = lista[0]
    jogo2 = lista[1]
    time1 = jogo1[0]
    time2 = jogo2[0]
    pontost1 = 0
    pontost2 = 0
    if jogo1[2][0] > jogo1[2][1]:
        pontost1 + 3, pontost2 + 0
    if jogo1[2][0] < jogo1[2][1]:
        pontost1 + 0, pontost2 + 3
    else:
        pontost1 + 1, pontost2 + 1
        if jogo2[2][0] > jogo1[2][1]:
            pontost1 + 0, pontost2 + 3
        if jogo2[2][0] < jogo1[2][1]:
            pontost1 + 3, pontost2 + 0
        else:
            pontost1 + 1, pontost2 + 1
            return {time1: pontost1, time2: pontost2}