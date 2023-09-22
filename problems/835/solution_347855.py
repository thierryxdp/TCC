def melhor_volta(matriz):
    menorestempos=[]
    colocado=menorestempos.index(min(menorestempos))
	volta=matriz[colocado+1].index(min(menorestempos))
    for i in range(len(matriz)):
        menor=min(matriz[i])
    menorestempos+=[menor]

	return(colocado+1,min(menorestempos),volta+1)