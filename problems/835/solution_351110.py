def melhor_volta(matriz):
    tempos = []
    for i in matriz:
        tempos.append(min(i))
	return(tempos.index(min(tempos)+1,1,min(tempos))