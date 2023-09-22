def pontos_por_time(x):
    c = x
    placar_jogo_1 = c[0][2]
    placar_jogo_2 = c[1[2]]
    if placar_jogo_1[0] > placar_jogo_1[1]:
        pontos_jogo_1 = 3
        total = {c[[0]]:3, c[0[1]]:0}
    elif placar_jogo_1[0] < placar_jogo_1[1]:
        pontos_jogo_1 = 3
        total = {c[0[0]]:0, c[0[1]]:3}
    else:
        pontos_jogo_1 = 1
        total = {c[0[0]]:1, c[0[1]]:1}
    if placar_jogo_2[0] > placar_jogo_2[1]:
        pontos_jogo_2 = 3
        total2 = {c[1[1]]:total[c[[0]]]+3, c[1[0]]:total[c[0[1]]]}
    elif placar_jogo_2[0] < placar_jogo_2[1]:
        pontos_jogo_2 = 3
        total2 = {c[1[1]]:total[c[0[0]]], c[1[0]]:total[c[0[1]]]+3}
    else:
        pontos_jogo_1 = 1
        total2 = {c[1[1]]:total[c[0[0]]]+1, c[1[0]]:total[c[0[1]]]+1}
        return total2