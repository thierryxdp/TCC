def pontos_por_time(jogo1,jogo2):
	timeA=[0][0]
    timeB=[0][1]
    pontosA= 0
    pontosB= 0 
    j1timeA=[0][2][0]
    j1timeB=[0][2][2]
    if j1timeA>j1timeB:
   		return pontosA+=3
    elif j1timeA<j1timeB:
    	return pontosB+=3
    else :
    	return pontosA+=1
		       pontosB+=1
    j2timeA=[1][2][1]
    j2timeb=[1][2][0]
    if j2timeA>j2timeb:
    	return pontosA+=3
    elif j2timeA<j2timeb:
    	return pontosB+=3
    elif:
    	return pontosA+=1
    		   pontosB+=1
    
    saldo={'timeA':pontosA,'timeB':pontosB}
    	return saldo