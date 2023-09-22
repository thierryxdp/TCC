def pontos_por_time(jogo1):
    time1=jogo1[0][0]
    time2=jogo1[0][1]
    pontos={str(time1): 0, str(time2): 0}
    if jogo1[0][2][0] > jogo1[0][2][1]:
        pontos[str(time1)] += 3
    if jogo1[0][2][0] < jogo1[0][2][1]:
        pontos[str(time2)]+= 3
    if jogo1[0][2][0] == jogo1[0][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    if jogo1[1][2][0] < jogo1[1][2][1]:
        pontos[str(time1)] += 3
    if jogo1[1][2][0] > jogo1[1][2][1]:
        pontos[str(time2)] += 3
    if jogo1[1][2][0] == jogo1[1][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    return pontos