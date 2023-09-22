def pontos_por_time(jogoi,jogov):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar;
    list, list -> dict"""
    time1 = jogoi[0]
    time2 = jogov[0]
	gols1 = jogoi[2][0]
	gols2 = jogoi[2][1] 
    gols3 = jogov[2][0]
    gols4 = jogov[2][1]
    
    if gols1>gols2 and gols3==gols4:
            return {time1:4, time2:1}