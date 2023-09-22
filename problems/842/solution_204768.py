def pontos_por_time(T):
	x=T[0]
    y=T[1]
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
    f=tuple(str(segundo_time)+": "+str(pontuacao_do_segundo_time)+', '+str(primeiro_time)+": "+str(pontuacao_do_primeiro_time))
	f={f}
    return f