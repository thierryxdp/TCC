def pontos_por_time(jogos):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar;
    list, list -> dict"""
    time11 = jogos[0][0]
    time12 = jogos[0][1]
	gols1 = jogos[0][2][0]
	gols2 = jogos[0][2][1] 
    gols3 = jogos[1][2][0]
    gols4 = jogos[1][2][1]
    
    if gols1<gols2 and gols3>gols4:
        return {time12:6, time11:0}
    elif gols1>gols2 and gols3>gols4:
        return {time11:3, time12:3}
    elif gols1<gols2 and gols3<gols4:
        return {time11:3, time12:3}
    elif gols1==gols2 and gols3<gols4:
        return {time11:4, time12:1}
    elif gols1>gols2 and gols3==gols4:
        return {time11:4, time12:1}
    elif gols1>gols2 and gols3<gols4:
        return {time12:0, time11:6}
    elif gols1==gols2 and gols3==gols4:
        return {time11:2, time12:2}