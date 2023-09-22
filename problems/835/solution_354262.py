def gera_matriz(nl, nc):
	lista = []

	for l in range(0, nl):
		nova = []
		lista.append(nova)
		for c in range(0, nc):
			n = random.uniform(1.0, 10.0)
			num = round(n,2)
			lista[l].append(num)
	return lista

def melhor_volta(matriz):
	ret = []
	corredor = 0
	tempo = 100000
	volta = 0
	
	for corr in range(0, len(matriz)):
		mini = min(matriz[corr])
		if tempo > mini:
			tempo = mini
			corredor = corr
			volta = matriz[corr].index(mini)

	ret.append(corredor)
	ret.append(tempo)
	ret.append(volta)

	return ret

m = [[6.44, 6.16, 8.12, 3.53, 8.2, 8.71, 3.81, 8.16, 8.68, 9.95], [9.19, 4.97, 4.35, 1.08, 8.66, 5.48, 2.48, 6.73, 7.15, 2.21], [3.41, 9.1, 3.59, 1.83, 7.61, 5.38, 7.99, 6.3, 9.43,