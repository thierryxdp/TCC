def pontos_por_time(jogos):
    time1_gol1 = jogos[0][2][0]
    time1_gol2 = jogos[1][2][1]
    time2_gol1 = jogos[0][2][1]
    time2_gol2 = jogos[1][2][0]
    resultado1 = time1_gol1 - time2_gol1
    resultado2 = time1_gol2 - time2_gol2
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    pontos = {}
    vitoria = 3
    derrota = 0
    empate = 1

    if resultado1 > 0 and resultado2 >0:
        pontos[time1] = (vitoria)*2
        pontos[time2] = derrota
        return pontos
    elif resultado1 > 0 and resultado2 == 0:
        pontos[time1] = (vitoria) + (empate)
        pontos[time2] = empate
        return pontos
    elif resultado1 == 0 and resultado2 == 0:
        pontos[time1] = (empate)*2
        pontos[time2] = (empate)*2
        return pontos
    elif resultado1 < 0 and resultado2 < 0:
        pontos[time1] = derrota
        pontos[time2] = (vitoria)*2
        return pontos
    elif resultado1 > 0 and resultado2 < 0:
        pontos[time1] = vitoria
        pontos[time2] = vitoria
        return pontos
    else:
        pontos[time1] = empate
        pontos[time2] = (empate)+ vitoria
        return pontos