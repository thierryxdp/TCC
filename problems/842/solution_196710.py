def pontos_por_time(jogoi,jogov):
    """Calcula os pontos dos times após dois jogos; list,list -> dict"""
    time_1 = jogoi[0]
    time_2 = jogov[0]
    pontos_time_1=0
    pontos_time_2=0
    if jogoi[2][0]>jogoi[2][1]:
        pontos_time_1+=3
    elif jogoi[2][0]<jogoi[2][1]:
        pontos_time_2+=3
    if jogov[2][1]>jogov[2][0]:
        pontos_time_1+=3
    elif jogov[2][1]<jogov[2][0]:
        pontos_time_2+=3
    if jogoi[2][0]==jogoi[2][1]:
        pontos_time_1+=1
        pontos_time_2+=1

        
    return {time_1:pontos_time_1, time_2:pontos_time_2}