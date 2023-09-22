def pontos_por_time(a,b):
    placar_jogo_1 = a[2]
    placar_jogo_2 = b[2]
    if placar_jogo_1[0] > placar_jogo_1[1]:
        pontos_jogo_1 = 3
        total = {a[0]:3, a[1]:0}
    elif placar_jogo_1[0] < placar_jogo_1[1]:
        pontos_jogo_1 = 3
        total = {a[0]:0, a[1]:3}
    else:
        pontos_jogo_1 = 1
        total = {a[0]:1, a[1]:1}
    if placar_jogo_2[0] > placar_jogo_2[1]:
        pontos_jogo_2 = 3
        total2 = {b[1]:total[a[0]]+3, b[0]:total[a[1]]}
    elif placar_jogo_2[0] < placar_jogo_2[1]:
        pontos_jogo_2 = 3
        total2 = {b[1]:total[a[0]], b[0]:total[a[1]]+3}
    else:
        pontos_jogo_1 = 1
        total2 = {b[1]:total[a[0]]+1, b[0]:total[a[1]]+1}
        return total2