def pontos_por_time(jogos):
    """Função que recebe uma lista de dois elementos, onde cada elemento é uma lista;
    cada lista possui informações iniciadas pelo time e placar;
    list, list -> dict"""
    time11 = jogos[0][0]
    time12 = jogos[0][1]
    time21 = jogos[1][0]
    time22 = jogos[1][1]
	gols1 = jogos[0][2][0]
	gols2 = jogos[0][2][1] 
    gols3 = jogos[1][2][0]
    gols4 = jogos[1][2][1]
    vitoria1 = gols1>gols2
    vitoria2 = gols1<gols2
    empate1 = gols1==gols2
    empate2 = gols3==gols4
    vitoria3 = gols3>gols4
    vitoria4 = gols3<gols4 
    
    if vitoria2 and vitoria3:
        return {time12:6, time22:0}
    if vitoria2 and vitoria4:
        return {time11:3, time21:3}
    if empate1 and vitoria4:
        return {time11:4, time21:1}
    if vitoria1 and vitoria3:
        return {time11:3, time21:3}
    if vitoria1 and empate2:
        return {time11:4, time21:1}
    if vitoria1 and vitoria4:
        return{time12:0, time22:6}
    if empate1 and empate2:
        return {time11:2, time21:2}