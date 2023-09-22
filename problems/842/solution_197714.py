def pontos_por_time(jogos):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar;
    list, list -> dict"""
    time11 = jogos[0][0]
    time12 = jogos[0][1]
    time21 = jogos[1][0]
    time22 = jogos[0][1]
	gols1 = jogos[0][2][0]
	gols2 = jogos[0][2][1] 
    gols3 = jogos[1][2][0]
    gols4 = jogos[1][2][1]
    
    if gols1<gols2 and gols3>gols4 and time12==time21:
        return {time12:6, time11:0}

    if gols1<gols2 and gols3<gols4 and time12==time21:
        return {time12:3, time11:3}
    if gols<gols2 and gols3<gols4 and time12!=time21:
        return {time11:3, time12:3}