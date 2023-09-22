def pontos_por_time(jogos):

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