pontos_por_time (jogoida,jogovolta)

jogos = dict()

#checa a quantidade de gols 
gols1_time1 = jogoida [2][:1]

gols1_time2 = jogoida [2][1:]
    
gols2_time1 = jogovolta [2][1:]

gols2_time2 = jogovolta [2][:1]

#times que estão jogando 

time1 = jogoida[0]

time2 = jogoida[1]

#

jogos['time'] = time1
jogos['time'] = time2

if gols1_time1 > gols1_time2

 return