def pontos_por_time(jogos):
    time1=jogos[0][0]
    time2=jogos[0][1]
    pontos={str(time1): 0, str(time2): 0}
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[str(time1)] += 3
    if jogos[0][2][0] < jogos[0][2][1]:
        pontos[str(time2)]+= 3
    if jogos[0][2][0] == jogos[0][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    if jogos[1][2][0] < jogos[1][2][1]:
        pontos[str(time1)] += 3
    if jogos[1][2][0] > jogos[1][2][1]:
        pontos[str(time2)] += 3
    if jogos[1][2][0] == jogos[1][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    return pontos