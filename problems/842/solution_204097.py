def pontos_por_time(jogos):
    timeA = jogos[0][0]
    timeB = jogos[0][1]
    
    pontosA = 0
    pontosB = 0
    if jogos[0][2][0] > jogos[0][2][1]:
        pontosA += 3
    elif jogos[0][2][0] == jogos[0][2][1]:
        pontosA += 1
        pontosB += 1
    else:
        pontosB += 3
    
    if jogos[1][2][1] > jogos[1][2][0]:
        pontosA += 3
    elif jogos[1][2][1] == jogos[1][2][0]:
    	pontosA += 1
        pontosB += 1
    else:
        pontosB += 3
    return {timeA: pontosA, timeB: pontosB}