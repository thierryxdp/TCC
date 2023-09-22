def pontos_por_time( informacoes ):
    time1 = informacoes[0][0]
    time2 = informacoes[0][1]
    pontos1 = 0
    pontos2 = 0
    if informacoes[0][2][0] > informacoes[0][2][1]:
        pontos1 += 3
    elif informacoes[0][2][0] < informacoes[0][2][1]:
        pontos2 += 3
    else:
        pontos1 += 1
        pontos2 += 1
        
    if informacoes[1][2][0] > informacoes[1][2][1]:
        pontos2 += 3
    elif informacoes[1][2][0] < informacoes[1][2][1]:
        pontos1 += 3
    else:
        pontos1 += 1
        pontos2 += 1
        
    return { time1 : pontos1, time2 : pontos2  }