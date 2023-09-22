def pontos_por_time(jogos):
    '''Dadas duas listas
    list -> dic'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    (jogo1_time1) = int(jogos[0][2][0])
    jogo1_time2 = int(jogos[0][2][1])
	if(jogo1_time1) > jogo1_time2:
        pontos1 = 3
        pontos2 = 0
 	elif jogo1_time1 == jogo1_time2:
        pontos1 = 1
        pontos1 = pontos2
 	if jogo1_time1 < jogo1_time2:
        pontos1 = 0
        pontos2 = 3
	return pontos1, pontos2