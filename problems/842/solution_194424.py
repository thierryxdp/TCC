def pontos_por_time(jogos):
    '''funcao que recebe uma lista de dois times, ambos sao uma lista'''
    '''list,list-> dic'''
	time1 = jogos[0][0]
    time2 = jogos[0][1]
    t1j1 = jogos[0][2][0]
    t2j1 = jogos[0][2][1]
    t1j2 = jogos[1][2][0]
    t2j2 = jogos[1][2][1]
    ponto1 = 0
    ponto2 = 0
    auxponto1 = 0
    auxponto2 = 0
    
    if t1j1 > t2j1:
        ponto1 = 3
    elif t2j1 > t1j1:
        ponto2 = 3
    else: 
        ponto1 = 1
        ponto2 = 1

    if t1j2 > t2j2:
        auxponto1 = 3
    elif t2j2 > t1j2:
        auxponto2 = 3
    else: 
        auxponto1 = 1
        auxponto2 = 1 
        
    if time1 == jogos[1][0]:
        ponto1 += auxponto1
        ponto2 += auxponto2
    else:
        ponto1 += auxponto2
        ponto2 += auxponto1

    if ponto1 = ponto2:
        return {time1:ponto1, time2:ponto2}
    else:
        return {time2:ponto2, time1:ponto1}