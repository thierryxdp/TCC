def pontos_por_time (jogo):
    if jogo jogo[0][2][0] > jogo[0][2][1]:
        x = 3
        w = 0
    if jogo jogo[0][2][0] == jogo[0][2][1]:
        x = 1
        w = 1
    if jogo jogo[0][2][0] < jogo[0][2][1]:
        x = 0
        w = 3
    if jogo jogo[1][2][1] > jogo[1][2][0]:
        y = 3
        z = 0
    if jogo jogo[1][2][1] == jogo[1][2][0]:
        y = 1
        z = 1
    if jogo jogo[1][2][1] < jogo[1][2][0]:
        y = 0
        z = 3
    return {jogo[0][0]: x+y, jogo[0][1]:w+z}