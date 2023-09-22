def melhor_volta(matriz):
	'''função que dada uma matriz 6x10 que represente os tempos em 
    segundos das 10 voltas de cada um dos 6 corredores de kart, retorne 
    de quem foi a melhor volta,com qual tempo e em que volta; 
    list-->tuple'''
	menor=[0,matriz[0][0],0]
	ncorredores=len(matriz)
	nvoltas=len(matriz[0])
	for corredor in range(ncorredores):
		if min(matriz[corredor])<menor[1]:
			menor[0]=corredor+1
			menor[1]=min(matriz[corredor])
			menor[2]=list.index(matriz[corredor],menor[1])+1
	resultado=(menor[0],menor[1],menor[2])
	return resultado