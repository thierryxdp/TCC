def pontos_por_time(lista_jogo1, lista_jogo2):
    pontuacao1_time1 = lista_jogo1[1][0]
    pontuacao1_time2 = lista_jogo1[1][1]
    
    pontuacao2_time1 = lista_jogo2[1][0]
    pontuacao2_time2 = lista_jogo2[1][1]
    
    time1 = lista_jogo1[0][0]
    time2 = lista_jogo1[0][1]
    
    if pontuacao1_time1 == pontuacao1_time2:
        soma_time1 = 1
        soma_time2 = 1
    if pontuacao1_time1 > pontuacao1_time2:
        soma_time1 = pontuacao1_time1*3
    if pontuacao1_time1 < pontuacao1_time2:
        soma_time2 = pontuacao1_time2*3
    
    if pontuacao2_time1 == pontuacao2_time2:
        soma_time1 = soma_time1 + 1
        soma_time2 = soma_time2 + 1
    if pontuacao2_time1 > pontuacao2_time2:
        soma_time1 = soma_time1 + pontuacao2_time1*3
    if pontuacao2_time1 < pontuacao2_time2:
        soma_time2 = soma_time2 + pontuacao2_time2*3
    return {time1: soma_time1, time2: soma_time2}