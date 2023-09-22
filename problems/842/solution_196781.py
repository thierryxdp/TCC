def pontos_por_time(resultado_jogos):
    resultado_jogo1=resultado_jogos[0]
    resultado_jogo2=resultado_jogos[1]
    times=resultado_jogo1[0]
    times=resultado_jogo2[0]
    time1=times[0]
    time2=times[1]
    pontos1=resultado_jogo1[1]
    pontos_time1_jogo1=pontos1[0]
    pontos_time2_jogo1=pontos1[1]
    pontos2=resultado_jogo1[1]
    pontos_time1_jogo2=pontos2[0]
    pontos_time2_jogo2=pontos2[1]
    pontos_parciais1=[ponto_parcial1_1,ponto_parcial2_1]
    pontos_parciais2=[ponto_parcial1_2,ponto_parcial2_2]
    if pontos_time1_jogo1>pontos_time2_jogo1:
        pontos_parciais1=[3,0]
    if pontos_time1_jogo1==pontos_time2_jogo1:
        pontos_parciais1=[1,1]
    if pontos_time1_jogo1<pontos_time2_jogo1:
        pontos_parciais1=[0,3]
    if pontos_time1_jogo2>pontos_time2_jogo2:
        pontos_parciais2=[3,0]
    if pontos_time1_jogo2==pontos_time2_jogo2:
        pontos_parciais2=[1,1]
	if pontos_time1_jogo2<pontos_time2_jogo2:
        pontos_parciais2=[0,3]
	pontos_finais=[pontos_parciais1[0]+pontos_parciais2[0],pontos_parciais1[1]+pontos_parciais2[1]]
	return [times, pontos_finais]