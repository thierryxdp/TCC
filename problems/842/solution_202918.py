def pontos_por_time(jogo_ida, jogo_volta):
    gols1 = (jogo_ida[2][0], jogo_ida[2][1]) 
  	gols2 = (jogo_volta[2][1], jogo_volta[2][0])
    Cormengo = jogo_ida[0]
    Flaminthians = jogo_ida[1]
    classificacao = {Cormengo:0, Flaminthians:0}
    if gols1[0] > gols1[1]:
        classificacao[Cormengo] += 3
    if gols1[0] == gols1[1]:
        classificacao[Cormengo] += 1
        classificacao[Flaminthians] += 1
    if gols1[0] < gols1[1]
    	classificacao[Flaminthians] += 3
        if gols2[0] > gols2[1]:
        classificacao[Cormengo] += 3
    if gols2[0] == gols2[1]:
        classificacao[Cormengo] += 1
        classificacao[Flaminthians] += 1
    if gols2[0] < gols2[1]
    	classificacao[Flaminthians] += 3