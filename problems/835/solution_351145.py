def melhor_volta(matriz):
    tupla = (0,min(matriz[0]),matriz[0].index(min(matriz[0])))
    for i in range(len(matriz)):
        if min(matriz[i]) < tupla[1]:
            tupla = (i+1,min(matriz[i]),matriz[i].index(min(matriz[i+1])))
	return tupla