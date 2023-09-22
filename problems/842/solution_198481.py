def pontos_por_time(placar):
	timeA=[0]
    timeB=[1]
    pontosA= 0
    pontosB= 0 
    j1timeA=[0][2][0]
    j1timeB=[0][2][2]
    if j1timeA>j1timeB:
        pontosA+=3
        return pontosA
    elif j1timeA<j1timeB:
        pontosB+=3
    	return pontosB
    else :
        pontosA+=1
        pontosB+=1
    	return pontosA and pontosB
    j2timeA=[1][2][1]
    j2timeb=[1][2][0]
    if j2timeA>j2timeb:
        pontosA+=3
    	return pontosA
    elif j2timeA<j2timeb:
        pontosB+3
    	return pontosB
    else:
        pontosA+=1
    	pontosB+=1
    	return pontosA and pontosB
    	saldo={'timeA':pontosA,'timeB':pontosB}
    	return saldo