def pontos_por_time(jogos):
    '''calcula a quantidade de pontos de dois times, dado dois jogos entre eles (jogos), e armazena esses dados em um dicionário
    list -> dict'''

    jogo1 = jogos[0]
    jogo2 = jogos[1]

    time1 = jogo1[0]
    time2 = jogo1[1]
    resultado1 = jogo1[2]
    resultado2 = jogo2[2]

    if resultado1[0] > resultado1[1]:
        pontos1 = 3
        pontos2 = 0
    elif resultado1[0] == resultado1[1]:
        pontos1 = 1
        pontos2 = 1
    else:
        pontos1 = 0
        pontos2 = 3

    if resultado2[0] > resultado2[1]:
        pontos1 += 0
        pontos2 += 3
    elif resultado2[0] == resultado2[1]:
        pontos1 += 1
        pontos2 += 1
    else:
        pontos1 += 3
        pontos2 += 0

    pontos_totais = {time1: pontos1, time2: pontos2}

    return pontos_totais