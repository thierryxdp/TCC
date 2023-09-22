def melhor_volta(matriz):
    menorestempos=[]
    
    for i in range(len(matriz)):
        menor=min(matriz[i])
    menorestempos+=[menor]
	colocado=menorestempos.index(min(menorestempos))+1
	volta=matriz[colocado].index(min(menorestempos))
	return(colocado,min(menorestempos),volta+1)