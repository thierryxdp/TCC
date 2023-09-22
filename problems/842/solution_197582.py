def pontos_por_time(jogos):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar;
    list, list -> dict"""
    time11 = jogos[0][0]
    time21 = jogos[0][1]
    time12 = jogos[1][0]
    time22 = jogos[1][1]
	gols1 = jogos[0][2][0]
	gols2 = jogos[0][2][1] 
    gols3 = jogos[1][2][0]
    gols4 = jogos[1][2][1]
    
    if gols1>gols2 and gols3>gols4:
        return {time11:3, time12:3}
    if gols1<gols2 and gols3>gols4:
        return {time12:6, time22:0}
    if gols1<gols2 and gols3<gols4:
        return {time11:3, time12:3}
    if gols1>gols2 and gols3<gols4:
        return{time11:6, time12:0}
    if gols1==gols2 and gols3<gols4:
        return {time11:4, time12:1}
    if gols1>gols2 and gols3<gols4:
        return {time11:3, time21:3}
    if gols1==gols2 and gols3==gols4:
        return {time11:2, time21:2}