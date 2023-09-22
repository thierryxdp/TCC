def pontos_por_time(x,y):
	primeiro_time=x[0]
    segundo_time=x[1]
    placar1=x[2]
    placar2=y[2]
    pontuacao_do_primeiro_time=0
    pontuacao_do_segundo_time=0
    if placar1[0]>placar1[1]:
        pontuacao_do_primeiro_time+=3
    if placar1[0]<placar1[1]:
        pontuacao_do_segundo_time+=3
    if placar2[0]>placar2[1]:
        pontuacao_do_segundo_time+=3
    if placar2[0]<placar2[1]:
        pontuacao_do_primeiro_time+=3
    f=segundo_time+':'+pontuacao_do_segundo_time+','+primeiro_time+':'+pontuacao_do_primeiro_time
	return f