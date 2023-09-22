def pontos_por_time(placares):
    """"""
    placar1 = placares[0]
    placar2 = placares[1]

    gols1 = placar1[2]
    gols2 = placar2[2]
    
    time1 = placar1[0]
    time2 = placar2[0]
    
    pontos_time1 = 0
    pontos_time2 = 0
    
    if gols1[0] > gols1[1]:
        pontos_time1 = pontos_time1+3
    elif gols1[0] < gols1[1]:
        pontos_time2 = pontos_time2+3
    elif gols1[0] == gols1[1]:
        pontos_time1 = pontos_time1 +1
        pontos_time2 = pontos_time2 +1
        
    if gols2[0] > gols2[1]:
        pontos_time2 =  pontos_time2+3
    elif gols2[0] < gols2[1]:
        pontos_time1 = pontos_time1+3
    elif gols2[0] == gols2[1]:
        pontos_time1 = pontos_time1 +1
        pontos_time2 = pontos_time2 +1
            
    pontuacao = {time1:pontos_time1, time2:pontos_time2}
    return pontuacao
    o