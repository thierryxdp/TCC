def pontos_por_time(partidas)
	'''função que, dado uma partida com dois jogos entre dois times, retorna a pontuação final de cada time
    	list -> dict'''
    pontos1=0
    pontos2=0

    if partida[0][2][0]>partida[0][2][1]:
        pontos1=pontos1+3
    elif partida[0][2][0]<partida[0][2][1]:
        pontos2= pontos2+3
    else:
        pontos1=1
        pontos2=1

    if partida[1][2][0]>partida[1][2][1]:
        pontos2=pontos2+3
    elif partida[1][2][0]<partida[1][2][1]:
        pontos1=pontos1+3
    else:
        pontos1=pontos1+1
        pontos2=pontos2+1
    return {partida[0][0]:pontos1,partida[0][1]:pontos2}