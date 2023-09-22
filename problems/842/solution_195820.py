#Start your python function here
def pontos_por_time(partida1, partida2):
    placar1 = partida1[2]
    time1_1 = partida1[0]
    time1_2 = partida1[1]
    time1_1_pontos
    time1_2_pontos
    
    placar2 = partida2[2]
    time2_1 = partida2[0]
    time2_2 = partida2[1]
    time2_1_pontos
    time2_2_pontos
    
    if(placar1[0]>placar1[1]):
        time1_1_pontos = 3
    if(placar1[0]<placar1[1]):
        time1_2_pontos = 3
    if(placar1[0]==placar1[1]):
        time1_1_pontos = 1
        time1_2_pontos = 1
        
   	if(placar2[0]>placar2[1]):
        time2_1_pontos = 3
    if(placar2[0]<placar2[1]):
        time2_2_pontos = 3
    if(placar2[0]==placar2[1]):
        time2_1_pontos = 1
        time2_2_pontos = 1
        
    time1_pontos
    time1_nome
    time2_pontos
    time2_nome
    
    if(time1_1 == time2_1):
        time1_pontos = time1_1_pontos + time2_1_pontos
        time2_pontos = time1_2_pontos + time2_2_pontos
        time1_nome = time1_1
        time2_nome = time1_2
    else:
        time1_pontos = time1_1_pontos + time2_2_pontos
        time2_pontos = time1_2_pontos + time2_1_pontos
        time1_nome = time1_2
        time2_nome = time1_1
        
    dic = {time1_nome : time1_pontos, time2_nome : time2_pontos}
        
    return dic