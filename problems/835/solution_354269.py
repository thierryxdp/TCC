def melhor_volta(matriz):
	corredor = 0
	tempo = 100000
	volta = 0
	
	for corr in range(0, len(matriz)):
		mini = min(matriz[corr])
		if tempo > mini:
			tempo = mini
			corredor = corr
			volta = matriz[corr].index(mini)

	corredor = corredor+1
	volta = volta+1

	return (corredor, tempo, volta)