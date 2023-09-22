def pontos_por_time(x):
    return {lst[0][1] : rodada(resultado1(lst[0][2])[1], resultado2(lst[1][2])[1]),
            lst[0][0] : rodada(resultado1(lst[0][2])[0], resultado2(lst[1][2])[0])}