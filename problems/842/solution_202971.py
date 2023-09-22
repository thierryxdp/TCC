def pontos_por_time(listas_jogo):
    
    pontuacao1_time1 = listas_jogo[0][2][0]
    pontuacao1_time2 = listas_jogo[0][2][1]
    
    pontuacao2_time1 = listas_jogo[1][2][0]
    pontuacao2_time2 = listas_jogo[1][2][1]
    
    time1 = listas_jogo[0][0]
    time2 = listas_jogo[0][1]
    
    soma_time1 = 0
    soma_time2 = 0
    
    if pontuacao1_time1 == pontuacao1_time2:
        soma_time1 = 1
        soma_time2 = 1
    if pontuacao1_time1 > pontuacao1_time2:
        soma_time1 = 3
    if pontuacao1_time1 < pontuacao1_time2:
        soma_time2 = 3
    
    if pontuacao2_time1 == pontuacao2_time2:
        soma_time1 = soma_time1 + 1
        soma_time2 = soma_time2 + 1
    if pontuacao2_time1 > pontuacao2_time2:
        soma_time1 = soma_time1 + 3
    if pontuacao2_time1 < pontuacao2_time2:
        soma_time2 = soma_time2 + 3
    
    return {time2: soma_time2, time1: soma_time1}