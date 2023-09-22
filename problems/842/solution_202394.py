def pontos_por_time(a):
#lista[lista[str,int,int],lista[str,int,int]--dicionário
	jogo1=a[0]
	jogo2=a[1]
	time1=jogo2[0]
	time2=jogo2[1]
	golsjogo1=jogo1[2]
	golsjogo2=jogo2[2]
	dic={time1:,time2:}
	if golsjogo1[0] > golsjogo1[1]:
		dic[time1]=3
	elif golsjogo1[0]<golsjogo1[1]:
		dic[time2]=3
	elif golsjogo1[0]=golsjogo1[1]:
		dic[time1]=1 and dic[time2]=1
	if golsjogo2[0]>golsjogo2[1]:
		dic[time1]=dic[time1]+3
	elif golsjogo2[0]<golsjogo2[1]:
		dic[time2]=dic[time2]+3
	elif golsjogo2[0]==golsjogo2[1]:
		dic[time2]=dic[time2]+1 and dic[time1]=dic[time1]+1
	return dic