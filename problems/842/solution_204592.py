def pontos_por_time(jogos):
    '''Retorna um dicionário com a pontuação final dos respectivos times dados como 
    entrada.'''

    ida, volta = jogos
    timeA = ida[0]
    timeB = ida[1]
    idaPontos = ida[2]
    voltaPontos = volta[2]
    pontuacao = [pontuacao[timeA] , pontuacao[timeB]]

    if idaPontos[0] > idaPontos[1]:
        pontuacao[timeA] += 3
    elif idaPontos[0] == idaPontos[1]:
        pontuacao[timeA] += 1
        pontuacao[timeB] += 1
    else:
        pontuacao[timeB] += 3
    if voltaPontos[0] > voltaPontos[1]:
        pontuacao[timeB] += 3
    elif voltaPontos[0] == voltaPontos[1]:
        pontuacao[timeB] += 1
        pontuacao[timeA] += 1
    else:
        pontuacao[timeA] += 3

    return {timeA: pontuacao[timeA] , timeB: pontuacao[timeB]}