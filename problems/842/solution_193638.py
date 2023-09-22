def pontos_por_time(gols):
    """ """
    ponto_a=0
    ponto_b=0
    gol_a_1=gols[0][2][0]
    gol_b_1=gols[0][2][1]
    gol_b_2=gols[1][2][0]
    gol_a_2=gols[1][2][1]
    time_a=gols[0][0]
    time_b=gols[0][1]
    resultado={}
    
    if gol_a_1>gol_b_1:
    	ponto_a+=3
    elif gol_a_1==gol_b_1:
    	ponto_a+=1
        ponto_b+=1
    else:
        ponto_b_=3
        
	if gol_a_2>gol_b_2:
    	ponto_a+=3
    elif gol_a_2==gol_b_2:
    	ponto_a+=1
        ponto_b+=1
    else:
        ponto_b_=3
    
    resultado[time_a]=ponto_a
    resultado[time_b]=ponto_b
    return resultado