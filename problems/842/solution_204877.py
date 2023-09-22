def pontos_por_time(jogos):
    gols1 = (jogos[1][2][0], jogos[1][2][1]) 
    gols2 = (jogos[0][2][1], jogos[0][2][0])
    time1 = jogos[1][0]
    time2 = jogos[1][1]
    classificacao = {time1:0, time2:0}
    if gols1[0] > gols1[1]:
        classificacao[time1] += 3
    if gols1[0] == gols1[1]:
        classificacao[time1] += 1
        classificacao[time2] += 1
    if gols1[0] < gols1[1]:
    	  classificacao[time2] += 3
    if gols2[0] > gols2[1]:
        classificacao[time1] += 3
    if gols2[0] == gols2[1]:
        classificacao[time1] += 1
        classificacao[time2] += 1
    if gols2[0] < gols2[1]:
    	  classificacao[time2] += 3
        
    return classificacao#Start your python function here