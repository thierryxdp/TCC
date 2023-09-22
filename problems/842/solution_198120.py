def pontos_por_time(jogos):
    """XXXXXXXXX"""
    jogo1 = jogos[0]
    jogo2 = jogos[1]

    time1 = jogo1[0]
    time2 = jogo1[1]

    pontos1 = 0
    pontos2 = 0

    #jogo1
    gols11 = jogo1[2][0]
    gols12 = jogo1[2][1]

    if (gols11 > gols12):
        pontos1 += 3
    elif (gols12 > gols11):
        pontos2 += 3

    elif (gols11 == gols12):
        pontos1 += 1
        pontos2 += 1

    #jogo2
    gols21 = jogo1[2][1]
    gols22 = jogo1[2][0]

    if (gols21 > gols22):
        pontos1 += 3
    elif (gols22 > gols21):
        pontos2 += 3

    elif (gols21 == gols22):
        pontos1 += 1
        pontos2 += 1

    return {time1:pontos1, time2:pontos2}