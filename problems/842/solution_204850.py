def pontos_por_time(jogo):
    if jogo[0][2][0] > jogo[0][2][1] and jogo[1][2][1] > jogo[1][2][0]:
        pontuacao = {jogo[0][0]:6, jogo[0][1]:0}
        return pontuacao
    elif jogo[0][2][0] < jogo[0][2][1] and jogo[1][2][1] < jogo[1][2][0]:
        pontuacao = {jogo[0][0]:0, jogo[0][1]:6}
        return pontuacao
    elif jogo[0][2][0] > jogo[0][2][1] and jogo[1][2][1] < jogo[1][2][0]:
        pontuacao = {jogo[0][0]:3, jogo[0][1]:3}
        return pontuacao
    elif jogo[0][2][0] == jogo[0][2][1] and jogo[1][2][1] == jogo[1][2][0]:
        pontuacao = {jogo[0][0]:1, jogo[0][1]:1}
        return pontuacao
    elif jogo[0][2][0] == jogo[0][2][1] and jogo[1][2][1] > jogo[1][2][0]:
        pontuacao = {jogo[0][0]:4, jogo[0][1]:1}
        return pontuacao
    elif jogo[0][2][0] == jogo[0][2][1] and jogo[1][2][1] < jogo[1][2][0]:
        pontuacao = {jogo[0][0]:1, jogo[0][1]:4}
        return pontuacao
    elif jogo[0][2][0] > jogo[0][2][1] and jogo[1][2][1] == jogo[1][2][0]:
        pontuacao = {jogo[0][0]:4, jogo[0][1]:1}
        return pontuacao
    elif jogo[0][2][0] < jogo[0][2][1] and jogo[1][2][1] == jogo[1][2][0]:
        pontuacao = {jogo[0][0]:1, jogo[0][1]:4}
        return pontuacao