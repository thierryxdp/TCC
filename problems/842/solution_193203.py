def pontos_por_time(jogos):
    '''Dadas duas listas
    list -> dic'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    jogo1_time1 = jogos[0][2][0]
    jogo1_time2 = jogos[0][2][1]
    pontos1 = 3
    pontos2 = 5
    
    dic = {time1:pontos1, time2:pontos2}
	return