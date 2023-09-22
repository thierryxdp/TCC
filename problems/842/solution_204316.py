def pontos_por_time(entrada):
    jogo1, jogo2 = entrada
    timeA, timeB, pnt1 = jogo1
    r0, r0, pnt2 = jogo2
    pnt_j1_A, pnt_j1_B = pnt1
    pnt_j2_B, pnt_j2_A = pnt2
    resultado = {timeA:0, timeB:0}
    
    if pnt_j1_A > pnt_j1_B:
        resultado[timeA] = 3
    	if pnt_j2_A > pnt_j2_B:
       		resultado[timeA] = 6
        if pnt_j2_B > pnt_j2_A:
       		resultado[timeB] = 3
        if pnt_j2_A = pnt_j2_B:
            resultado = {timeA:4, timeB:1}
    if pnt_j1_B > pnt_j1_A:
        resultado[timeB] = 3
    	if pnt_j2_A > pnt_j2_B:
       		resultado[timeA] = 3
        if pnt_j2_B > pnt_j2_A:
       		resultado[timeB] = 6
        if pnt_j2_A = pnt_j2_B:
            resultado = {timeA:1, timeB:4}
    if pnt_j1_A = pnt_j1_B
    	resultado[timeB] = 1
        resultado[timeA] = 1
    	if pnt_j2_A > pnt_j2_B:
       		resultado[timeA] = 4
        if pnt_j2_B > pnt_j2_A:
       		resultado[timeB] = 4
    
    return resultado