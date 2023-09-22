def pontos_por_time(a):
#lista[lista[str,int,int],lista[str,int,int]--dicionário
	jogo1=a[0]
	jogo2=a[1]
	time1=jogo2[0]
	time2=jogo2[1]
	golsjogo1=jogo1[2]
	golsjogo2=jogo2[2]
	x=z
	if int(golsjogo1[0]) > int(golsjogo1[1]):
		z=3
	elif int(golsjogo1[0])<int(golsjogo1[1]):
		y=3
	elif int(golsjogo1[0])==int(golsjogo1[1]):
		golsjogo1[0]=1 and golsjogo1[1]=1
	
	if golsjogo2[0]>golsjogo2[1]:
		time2jogo2==time2jogo2+3 
	elif golsjogo2[0]<golsjogo2[1]:
		time1jogo2==time1jogo2+3
	elif golsjogo2[0]==golsjogo2[1]:
		time1jogo2==time1jogo2+1 and time2jogo2==time2jogo2+1
	
	return {time1:time1jogo1+time1jogo2,time2:time2jogo1+time2jogo2}