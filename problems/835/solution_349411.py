from math import inf
def melhor_volta(matriz):
    """Função que ao receber uma matriz com tempos de uma corrida de kart,
    retorna quem fez a melhor volta da corrida, o tempo da volta e em que
    volta;
    list -> bool"""
    placar = [0,inf,0]
	for i in range(len(matriz)):
   		for j in range(len(matriz[0])):
			if matriz[i][j] < placar[1]:
                placar = (i+1,matriz[i][j],j+1)
	return placar