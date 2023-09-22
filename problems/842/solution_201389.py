def pontos_por_time(jogos):
jogo1 = jogos[0][2][0] + jogos[1][2][0]
jogo2 = jogos[0][2][1] + jogos[1][2][1]
    if jogo1>jogo2:
        return jogos[0][0]