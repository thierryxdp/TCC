def melhor_volta(matriz:list[list])->tuple:
    tempo, corredor, volta, indice = 1000, 0, 0, 0
    for i in matriz:
        if min(i) < tempo:
            corredor = indice
            tempo = min(i)
            volta = i.index(tempo)
        indice += 1
	return (corredor, tempo, volta)