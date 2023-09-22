jogo1=a[0]
jogo2=a[1]
time1=jogo1[0]
time2=jogo2[1]
gols2=jogo2[2]
gols1=jogo1[2]
dic={time1:0,time2:0}
if gols1[0]>gols1[1]:
    dic[time2]=3
elif gols1[0]<gols1[1]:
	dic[time1]=3
else:
	dic[time2]=1
	dic[time1]=1
	
if gols2[0]<gols2[1]:
	dic[time2]=dic[time2]+3
elif gols2[0]>gols2[1]:
	dic[time1]=dic[time1]+3
else:
	dic[time2]=dic[time2]+1
	dic[time1]=dic[time1]+1
    return dic