def pontos_por_time(jogo1,jogo2)
	if jogo1[0]>jogo1[1]:
    	return vitoria_cormengo
    elif jogo1[0]<jogo1[1]:
    	return vitoria_Flaminthians
    else:
    	return empate
    if jogo2[0]>jogo2[1]:
    	return vitoria_cormengo
    elif jogo2[0]<jogo2[1]:
    	return vitoria_Flaminthians
    else:
    	return empate 
    vitoria_Flaminthians= 3
    vitoria_cormengo=3
    empate=1
    pontos1=[cormengo:jogo1+jogo2]
    pontos2=[flaminthians:jogo1+jogo2]
    saldo=[pontos1, pontos2]
    return saldo