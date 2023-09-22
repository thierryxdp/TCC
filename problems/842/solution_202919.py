def pontos_por_time(jogo_ida, jogo_volta):
    gols1 = (jogo_ida[2][0], jogo_ida[2][1]) 
  	gols2 = (jogo_volta[2][1], jogo_volta[2][0])
    time1 = jogo_ida[0]
    time2 = jogo_ida[1]
    classificacao = {time1:0, time2:0}
    if gols1[0] > gols1[1]:
        classificacao[time1] += 3
    if gols1[0] == gols1[1]:
        classificacao[time1] += 1
        classificacao[time2] += 1
    if gols1[0] < gols1[1]
    	classificacao[time2] += 3
        if gols2[0] > gols2[1]:
        classificacao[time1] += 3
    if gols2[0] == gols2[1]:
        classificacao[time1] += 1
        classificacao[time2] += 1
    if gols2[0] < gols2[1]
    	classificacao[time2] += 3
        
        return classificacao