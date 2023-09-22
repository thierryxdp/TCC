def pontos_por_time(jogo1)
	ponto1 = 0 ponto2 = 0
    if jogo1[0][2][0] > jogo1 [0][2][1]:
    	ponto1 +=3
    elif jogo1[0][2][0] < jogo1 [0][2][1]:
    	ponto2 +=3
    else ponto1 +=1 ponto2 +=1
    if jogo1[1][2][0] > jogo1 [1][2][1]:
    	ponto2 +=3
    elif jogo1[1][2][0] < jogo1 [1][2][1]:
    	ponto1 +=3
    else ponto1 +=1 ponto2 +=1
  	return {jogo1[0][0]: ponto1, jogo1[0][1]: ponto2 }