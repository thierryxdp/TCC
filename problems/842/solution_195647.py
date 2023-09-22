def pontos_por_time (lista_jogos):
"""Calcula e retorna a pontuação de dois times depois de uma rodada 
	mata-mata
    list -> dict"""
	jogo1=lista_jogos[0]
    jogo2=lista_jogos[1]
    time1=jogo1[0]
    time2=jogo1[1]
    placar1=jogo1[2]
    placar2=jogo2[2]
    pontos_time1=0
    pontos_time2=0
    if int(placar1[0])>int(placar1[1]):
        pontos_time1=pontos_time1+3
        pontos_time2=pontos_time2+0
    elif int(placar1[0])==int(placar1[1]):
        pontos_time1=pontos_time1+1
        pontos_time2=pontos_time2+1
    else: 
        pontos_time1=pontos_time1+0
        pontos_time2=pontos_time2+3
    if int(placar2[0])>int(placar2[1]):
        pontos_time2=pontos_time2+3
        pontos_time1=pontos_time1+0
    elif int(placar2[0])==int(placar2[1]):
        pontos_time2=pontos_time2+1
        pontos_time1=pontos_time1+1
    else: 
        pontos_time2=pontos_time2+0
        pontos_time1=pontos_time1+3
    pontuacao={time1:pontos_time1,time2:pontos_time2}
    return (pontuacao)