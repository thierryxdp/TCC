def pontos_por_time(resultado_jogo1, resultado_jogo2):
    resultado_jogo1=[times,pontos1]
    times=[time1,time2]
    pontos1=[pontos_time1_jogo1,pontos_time2_jogo1]
    pontos2=[pontos_time1_jogo2,pontos_time2_jogo2]
  	pontos_parciais1=[ponto_parcial1_1,ponto_parcial2_1]
    pontos_parciais2=[ponto_parcial1_2,ponto_parcial2_2]
    pontos_finais=pontos_parciais1+pontos_parciais2
    if pontos_time1_jogo1>pontos_time2_jogo1:
        pontos_parcias1=[3,0]
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
	return [times, pontos_finais]