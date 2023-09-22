def pontos_por_time (jogo):
    if jogo[0][2] > jogo[0][3]:
        x = 3  and w = 0
    if jogo[0][2] == jogo[0][3]:
        x = 1 and w = 1
    if jogo[0][2] < jogo[0][3]:
        x = 0 and w = 0
    if jogo[1][2] < jogo[1][3]:
        y = 3
z = 0
    if jogo[1][2] == jogo[1][3]:
        y = 1
z = 1
    if jogo[1][2] > jogo[1][3]:
        y = 0
z = 3
    return {jogo[0][0], jogo[0][1]}