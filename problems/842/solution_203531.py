def pontos_por_time(jogos):
    jogo1 = jogos[0]
    jogo2 = jogos[1]
    time1 = jogo1[0]
    time2 = jogo1[1]
    pontuacao1 = jogo1[2]
    pontuacao2 = jogo2[2]
    if pontuacao1[0] > pontuacao1[1]:
        pontosT1 = 3
        pontosT2 = 0
    elif pontuacao1[0] == pontuacao1[1]:
        pontosT1 = 1
        pontosT2 = 1
    else:
        pontosT1 = 0
        pontosT2 = 3
    if pontuacao2[1] > pontuacao2[0]:
        pontosT1 = pontosT1 + 3
    elif pontuacao2[1] == pontuacao2[0]:
        pontosT1 = pontosT1 + 1
        pontosT2 = pontosT2 + 1
    else:
        pontosT2 = pontosT2 + 3
    return [time1: pontosT1,time2: pontosT2]