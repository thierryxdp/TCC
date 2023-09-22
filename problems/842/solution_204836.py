def pontos_por_time(jogos):
    time1 = jogos[0]
    time2 = jogos[1]
    pontos1 = 0
    pontos2 = 0
    if (jogos[0][2][0] > jogos[0][2][1]):
        pontos1 += 3
    elif (jogos[0][2][0] < jogos[0][2][1]):
        pontos2 += 3
    else:
        pontos1 += 1
        pontos2 += 1
        
    if (jogos[1][2][list.index(jogos[1],time1)] > jogos[1][2][list.index(jogos[1],time2)]):
        pontos1 += 3
    elif (jogos[1][2][list.index(jogos[1],time1)] == jogos[1][2][list.index(jogos[1],time2)]):
        pontos1 += 1
        pontos2 += 1
    else:
        pontos2 += 3