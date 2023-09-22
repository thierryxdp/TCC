def melhor_volta(matriz):
	for i in range(len(matriz)):
		corredor_atual = 0
		for j in matriz[i]:
			corredor_atual += j