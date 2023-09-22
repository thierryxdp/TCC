def pontos_por_time(a):
#lista[lista[str,int,int],lista[str,int,int]--dicionário
	jogo1=a[0]
	jogo2=a[1]
	time1=jogo2[0]
	time2=jogo2[1]
	gols_jogo1=jogo1[2]
	gols_jogo2=jogo2[2]
	if gols_jogo1[0]>gols_jogo1[1]:
		time2vit1=3 and time1vit1=0
	elif gols_jogo1[0]<gols_jogo1[1]:
		time1vit1=3 and time2vit1=0
	elif gols_jogo1[0]==gols_jogo1[1]:
		time1vit1=1 and time2vit1=1
	
	if gols_jogo2[0]>gols_jogo2[1]:
		time2vit2=3 and time1vit2=0
	elif gols_jogo2[0]<gols_jogo2[1]:
		time1vit2=3 and time2vit2=0
	elif gols_jogo2[0]==gols_jogo2[1]:
		time1vit2=1 and time2vit2=1
	return {time1:time1vit1+time1vit2,time2:time2vit1+time2vit2}