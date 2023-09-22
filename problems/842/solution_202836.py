#a funcao retorna quantos pontos o time fez na fase 
#lista(str, str, lista(int, int)), lista(str, str, lista(int, int))->dicionario
def pontos_por_time(a):
	jogo1=a[0]
	jogo2=a[1]
	time1=jogo2[0]
	time2=jogo2[1]
	gols1=jogo1[2]
	gols2=jogo2[2]
	pontos={time1:0,time2:0}
    if gols1[0]>gols1[1]:
		pontos[time2]=3
    elif gols1[0]<gols1[1]:
		pontos[time1]=3
	else:
		pontos[time1]=1
		pontos[time2]=1
	
	if gols2[0]<gols2[1]:
		pontos[time2]=dic[time2]+3
    elif gols2[0]>gols2[1]:
		pontos[time1]=dic[time1]+3
	else:
		pontos[time1]=dic[time1]+1
	    pontos[time2]=dic[time2]+1
	return pontos