def melhor_volta(matriz):
    menorestempos=[]
    colocado=menorestempos.index(min(menorestempos))+1
	volta=matriz[colocado].index(min(menorestempos))
    for i in range(len(matriz)):
        menor=min(matriz[i])
    menorestempos+=[menor]

	return(colocado,min(menorestempos),volta+1)