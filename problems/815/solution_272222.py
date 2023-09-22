def pontos_por_time(jogos):
    '''
        Função que recebe uma lista e calcula os pontos dos times
        Cormengo e flamintians obtidos em 2 jogos, Retorna um dicionário
        contendo o time na chaves e seus pontos obtidos cada fase nos valores,
        onde cada vitória do time vale 3 pontos,empate vale 1 ponto pra ambos
        e no caso de derrota não vale nenhum ponto.
        list --> dict
    '''

    time1 = jogos[0][0]
    time2 = jogos[0][1]
    pontuacao1 = jogos[0][2][0]
    pontuacao2 = jogos[0][2][1]

    time_1 = jogos[1][1]
    time_2 = jogos[1][0]
    pontuacao_1 = jogos[1][2][1]
    pontuacao_2 = jogos[1][2][0]

    if pontuacao1>pontuacao2 and pontuacao_1>pontuacao_2:
        return {time2:0, time1:6}

    elif pontuacao2>pontuacao1 and pontuacao_2>pontuacao_1
        return {time2:6, time1:0}

    elif (pontuacao1>pontuacao2 and pontuacao_2>pontuacao_1) or (pontuacao2>pontuacao1 and pontuacao_1>pontuacao_2):
        return (time2:3, time1:3)

    elif pontuacao1 == pontuacao2 and pontuacao_1 == pontuacao_2:
        return {time2:2, time1:2}

    elif (pontuacao1>pontuacao2 and pontuacao_1 == pontuacao_2) or (pontuacao1 == pontuacao2 and pontuacao_1 > pontuacao_2):
        return {time2:1, time1:4}

    else (pontuacao2>pontuacao1 and pontuacao_1 == pontuacao_2) or (pontuacao1 == pontuacao2 and pontuacao_2 > pontuacao_1):
        return {time2:4, time1:1}