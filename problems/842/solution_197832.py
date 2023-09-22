def pontuacao(placar):
    if placar[0] == placar[1]:
        return 1,1
    elif placar[0] > placar[1]:
        return 3,0
    else:
        return 0,3
def pontos_por_time(jogos):
    pont = {}
    for time1, time2, placar in jogos:
	    p1,p2 = pontuacao(placar)
	    pont[time1] = pont.get(time1,0) + p1
	    pont[time2] = pont.get(time2,0) + p2
    return pont