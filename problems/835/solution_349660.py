def melhor_volta(matriz:list[list])->tuple:
    tempo, corredor, volta, indice = 1000, 0, 0, 1
    for i in matriz:
        if min(i) < tempo:
            corredor = indice
            tempo = min(i)
            volta = i.index(tempo)+1
        indice += 1
	return (corredor, tempo, volta)