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
    vitoria1 = gols1>gols2
    vitoria2 = gols1<gols2
    empate1 = gols1==gols2
    empate2 = gols3==gols4
    vitoria3 = gols3>gols4
    vitoria4 = gols3<gols4 
    
    if vitoria2 and vitoria3:
        return {time21:0}