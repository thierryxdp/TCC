def pontos_por_time(jogoi,jogov):
    """Calcula os pontos dos times após dois jogos; list,list -> dict"""
    time_1 = jogoi[0][0]
    time_2 = jogov[0][0]
    pontos_time_1=0
    pontos_time_2=0
    if jogoi[1][0]>jogoi[1][1]:
        pontos_time_1+=3
    elif jogo1[1][0]<jogoi[1][1]:
        pontos_time_2+=3
    elif jogov[1][1]>jogov[1][0]:
        pontos_time_1+=3
    elif jogov[1][1]<jogov[1][0]:
        pontos_time_2+=3
    if jogoi[1][0]==jogoi[1][1]:
        pontos_time_1+=1
        pontos_time_2+=1
    if jogov[1][1]==jogov[1][0]:
        pontos_time_1+=1
        pontos_time_2+=1
        
    return {time_1:pontos_time_1, time_2:pontos_time_2}