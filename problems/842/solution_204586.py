def pontos_por_time(jogos):

    ida, volta = jogos
    timeA = ida[0]
    timeB = ida[1]
    idaPontos = ida[2]
    voltaPontos = volta[2]

    if ida[0] > ida[1]:
       pontuacao[timeA] += 3
    elif ida[0] == ida[1]:
       pontuacao[timeA] += 1
       pontuacao[timeB] += 1
    else:
       pontuacao[timeB] += 3
    if volta[0] > volta[1]:
       pontuacao[timeB] += 3
    elif volta[0] == volta[1]:
       pontuacao[timeB] += 1
       pontuacao[timeA] += 1
    else:
       pontuacao[timeA] += 3

    return {timeA: pontuacao[timeA] , timeB: pontuacao[timeB]}