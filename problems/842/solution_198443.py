def pontos_por_time(jogo1,jogo2):
	if jogo1[0]>jogo1[1]:
    	return vitoria_casa
    elif jogo1[0]<jogo1[1]:
    	return vitoria_fora
    else:
    	return empate
    if jogo2[0]>jogo2[1]:
    	return vitoria_casa
    elif jogo2[0]<jogo2[1]:
    	return vitoria_fora
    else:
    	return empate 
    vitoria_casa= 3
    vvitoria_fora=3
    empate=1
    pontos1=[jogo1+jogo2]
    pontos2=[jogo1+jogo2]
    saldo=[pontos1, pontos2]
    return saldo