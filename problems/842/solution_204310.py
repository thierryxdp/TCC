def pontos_por_time(jogo1,jogo2):
    timeA, timeB, pnt1 = jogo1
    timeB, timeA, pnt2 = jogo2
    pnt_j1_A, pnt_j1_B = pnt1
    pnt_j2_B, pnt_j2_A = pnt2
    resultado = {timeA:0, timeB:0}
    
    if pnt_j1_A > pnt_j1_B:
        timeA += 3
    	if pnt_j2_A > pnt_j2_B:
       		timeA += 3
        if pnt_j2_B > pnt_j2_A:
       		timeB += 3
    if pnt_j1_B > pnt_j1_A:
        timeA += 3
    	if pnt_j2_A > pnt_j2_B:
       		timeA += 3
        if pnt_j2_B > pnt_j2_A:
       		timeB += 3
    return resultado