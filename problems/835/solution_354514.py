def melhor_volta(matriz):
    '''Retorna uma tupla contendo o autor da melhor volta, em quanto 
    tempo ela foi feita e em que volta foi realizada, com base na 
    matriz 6x10 inserida; list -> tuple(str, int, int)'''
    menor=min(matriz[0])
    cara=0
    for i in range(len(matriz)):
        if min(matriz[i])<=menor:
            menor=min(matriz[i])
            cara=i+1
    melhor=(cara, menor, list.index(menor)+1)
	return melhor