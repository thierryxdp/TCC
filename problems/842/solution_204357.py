def pontos_por_time (jogo):
    if jogo[0][2] > jogo[0][3]:
        (x = 3)
(w = 0)
    if jogo[0][2] == jogo[0][3]:
        x = 1
w = 1
    elif jogo[0][2] < jogo[0][3]:
        x = 0
w = 0
    elif jogo[1][2] < jogo[1][3]:
        y = 3
z = 0
    elif jogo[1][2] == jogo[1][3]:
        y = 1
z = 1
    elif jogo[1][2] > jogo[1][3]:
        y = 0
z = 3
    return {jogo[0][0], jogo[0][1]}