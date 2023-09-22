def melhor_volta(matriz):
	'''Função que dada uma matriz com 6 linhas e 10 colunas, considerando
	as linhas como os corredores, as colunas como as voltas e os elementos 
	como o tempo em segundos de cada corredor numa corrida de kart, retornando 
	de qual corredor dentre os 6 foi a melhor volta com qual tempo e em que volta. 
	Entrada: lista de listas
	Saída: tupla'''
	tupla = (0,float('inf'),0)
	for i in range(6):
		for j in range(10):
			if matriz[i][j] < tupla[1]:
				tupla = (i+1,matriz[i][j],j+1)
	return tupla