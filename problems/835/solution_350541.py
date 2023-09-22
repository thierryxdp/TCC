def melhor_volta(matriz):
    '''Função que recebe como entrada uma matriz 6 × 10 com os tempos em segundos dos corredores
	6 corredores nas 10 volta e retorna uma tupla contendo de quem foi a melhor volta,
    qual o tempo dessa volta e qual foi essa volta
    list -> tuple'''
    tempo_min = matriz[0][0]
    corredor = 0
    volta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
    		if tempo_min > matriz[i][j]:
                tempo_min = matriz[i][j]
                corredor = i
                volta = j
	return (corredor + 1, tempo_min, volta + 1)