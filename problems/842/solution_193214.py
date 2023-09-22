def pontos_por_time(jogos):
    '''Dadas duas listas
    list -> dic'''
    time1 = jogos[0][0]
    time2 = jogos[0][1]
    jogo1_time1 = jogos[0][2][0]
    jogo1_time2 = jogos[0][2][1]
    jogo2_time1 = jogos[1][2][0]
    jogo2_time2 = jogos[1][2][1]
	j1_t1 = 0
    j1_t2 = 0
    if jogo1_time1 == jogo1_time2:
        j1_t1 = 0
        j1_t2 = 0
   	if jogo1_time1 > jogo1_time2:
        j1_t1 = 3
   	if jogo1_time1 < jogo1_time2:
       	j1_t2 = 3
  	
    pontos1_total = j1_t1 + j2_t1
    pontos2_total = j1_t2 + j2_t2
    dic = {time1:pontos1_total, time2:pontos2_total}
	return dic