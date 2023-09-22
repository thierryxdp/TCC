#Start your python function here
def pontos_por_time(jogos):
    """Função que retorna o número de pontos marcados por dois times em uma fase
    de um campeonato dados seus nomes e a quantidade de gols marcados por cada um
    nas partidas de ida e de volta. Uma vitória concede 3 e um empate apenas 1 
    ponto. Derrotas não conferem pontos. O formato de inserção é a seguinte lista:
    [['time1','time2',[gols_t1,gols_t2]],['time2','time1',[gols_t2,gols_t1]]]
    lista[lista[string,string,lista],lista[string,string,lista]]->dict"""
    jogoi=jogos[0]
    jogov=jogos[1]
    t1=jogoi[0]
    t2=jogoi[1]
    gols_jogoi=jogoi[2]
    gols_jogov=jogov[2]
    gols_t1_jogoi=gols_jogoi[0]
    gols_t2_jogoi=gols_jogoi[1]
    gols_t1_jogov=gols_jogov[1]
    gols_t2_jogov=gols_jogov[0]
    if gols_t1_jogoi>gols_t2_jogoi:
        pts_t1_jogoi=3
        pts_t2_jogoi=0
	elif gols_t1_jogoi<gols_t2_jogoi:
        pts_t1_jogoi=0
        pts_t2_jogoi=3
	elif gols_t1_jogoi==gols_t2_jogoi:
        pts_t1_jogoi=1
        pts_t2_jogoi=1
	if gols_t1_jogov>gols_t2_jogov:
        pts_t1_jogov=3
        pts_t2_jogov=0
	elif gols_t1_jogov<gols_t2_jogov:
        pts_t1_jogov=0
        pts_t2_jogov=3
	elif gols_t1_jogoi==gols_t2_jogoi:
        pts_t1_jogov=1
        pts_t2_jogov=1
	return {t1:(pts_t1_jogoi+pts_t1_jogov),t2:(pts_t2_jogoi+pts_t2_jogov)}