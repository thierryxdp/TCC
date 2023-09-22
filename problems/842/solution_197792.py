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
    vitoria11 = gols1>gols2
    vitoria12 = gols2>gols1
    vitoria21 = gols1<gols2
    vitoria22 = gols2<gols1
    empate1 = gols1==gols2
    empate2 = gols3==gols4
    vitoria31 = gols3>gols4
    vitoria32 = gols4>gols3
    vitoria41 = gols3<gols4
    vitoria42 = gols4<gols3
    
    if vitoria21 and vitoria31:
        return {time12:6, time22:0}
    if vitoria21 and vitoria41:
        return {time12:3, time22:3}
    if vitoria12 and vitoria41:
        return {time11:3, time21:3}
    if empate1 and vitoria41:
        return {time11:4, time21:1}
    if vitoria21 and vitoria41:
        return {time11:3, time21:3}
    if vitoria11 and vitoria31:
        return {time12:3, time22:3}
    if vitoria11 and empate2:
        return {time11:4, time21:1}