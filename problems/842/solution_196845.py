def pontos_por_time(fase):
    """"""
    time1 = jogo1[0]
    time2 = jogo1[1]
    placar1 = jogo1[2]
    placar2 = jogo2[2]
    pontos_time1 = ()
    pontos_time2 = ()
    
    if placar1[0] > placar1[1]:
        pontos_time1 = pontos_time1+3
    elif placar1[0] < placar1[1]:
        pontos_time2 = pontos_time2+3
    elif placar1[0] == placar1[1]:
        pontos_time1 = pontos_time1 +1
        pontos_time2 = pontos_time2 +1
        
    if placar2[0] > placar2[1]:
        pontos_time2 =  pontos_time2+3
    elif placar2[0] < placar2[1]:
        pontos_time1 = pontos_time1+3
    elif placar1[0] == placar1[1]:
        pontos_time1 = pontos_time1 +1
        pontos_time2 = pontos_time2 +1
            
    pontuacao = {time1:pontos_time1, time2:pontos_time2}
    return pontuacao