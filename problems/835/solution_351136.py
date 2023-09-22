def melhor_volta(matriz):
    tempos = []
    pos = 0
    for i in matriz:
        tempos.append(min(j))
	for i in matriz:
        if min(tempos) in i:
            for j in i:
                if j != min(tempos):
                    pos+=1
                else:
                    break
	return(matriz.index(min(tempos)+1,min(tempos),pos))