def pontos_por_time(jogos):
    """Calcula os pontos dos times após dois jogos; list,list -> dict"""
    time_1 = jogos[0][0]
    time_2 = jogos[1][0]
    pontos_time_1=0
    pontos_time_2=0
    if jogos[0][2][0]>jogos[0][2][1]:
        pontos_time_1+=3
    if jogos[0][2][0]<jogos[0][2][1]:
        pontos_time_2+=3
    if jogos[1][2][1]>jogos[1][2][0]:
        pontos_time_1+=3
    if jogos[1][2][1]<jogos[1][2][0]:
        pontos_time_2+=3
    if jogos[0][2][0]==jogos[0][2][1]:
        pontos_time_1+=1
        pontos_time_2+=1
    if jogos[1][2][0]==jogos[1][2][1]:
        pontos_time_1+=1
        pontos_time_2+=1

        
    return {time_1:pontos_time_1, time_2:pontos_time_2}#Start your python function here