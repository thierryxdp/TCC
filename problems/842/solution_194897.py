def pontos_por_time (jogos):
    jogoida = jogos[0]
    jogovolta = jogos[1]
    jogoida[0] = time1
    jogoida[1] = time2
    jogoida[2] = placar1
    jogovolta[2] = placar2
    if placar1[0] > placar1 [-1]:
        pontos_time1 = 3
        pontos_time2 = 0
	elif placar1[0] < placar1 [-1]:
        pontos_time1 = 0
        pontos_time2 = 3
	else:
        pontos_time1 = 1
        pontos_time2 = 1
	if placar2[0] > placar2 [-1]:
        pontostime2 += 3
	elif placar2[0] < placar2 [-1]:
        pontos_time1 += 3
	else:
        pontos_time1 += 1
        pontos_time2 += 1
	tabela = {time1:pontos_time1,time2:pontos_time2}
    return tabela