def melhor_volta(matriz):
    melhor_tempo = 0
    tupla = (0,0,0)
    for i in matriz:
        for j in i:
            if j > melhor_tempo:
                melhor_tempo = j
                tupla = (matriz.index(i)+1,melhor_tempo,i.index(j)+1)
	return tupla