def pontos_por_time(placar):
	timeA=placar[0][0]
    timeB=placar[0][1]
    pontosA= 0
    pontosB= 0 
    j1timeA=placar[0][2][0]
    j1timeB=placar[0][2][1]
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
    j2timeA=placar[1][2][1]
    j2timeb=placar[1][2][0]
    if j2timeA>j2timeb:
        pontosA+=3
    	return pontosA
    elif j2timeA<j2timeb:
        pontosB+=3
    	return pontosB
    else:
        pontosA+=1
    	pontosB+=1
    	return pontosA and pontosB
    	saldo=[timeA:pontosA,timeB:pontos]
    return saldo