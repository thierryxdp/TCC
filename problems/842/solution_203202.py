#Start your python function here
def pontos_por_time(jogos):
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    
    pontos1 = 0
    pontos2 = 0
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos1 += 3
    elif jogos[0][2][0] == jogos[0][2][1]:
        pontos1 += 1
        pontos2 += 1
    else:
        pontos2 += 3
    
    if jogos[1][2][1] > jogos[1][2][0]:
        pontos1 += 3
    elif jogos[1][2][1] == jogos[1][2][0]:
    	pontos1 += 1
        pontos2 += 1
    else:
        pontos2 += 3
    return {time1: pontos1, time2: pontos2}