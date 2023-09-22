def melhor_volta(voltas):
    '''identifica qual foi a melhor volta, o tempo dela e o corredor que a 
    realizou numa corrida'''
    melhor_cada = []
    for i in range(0, 6):
    	melhor_cada.append(min(voltas[i]))
    	for j in range(0, 10):
	        melhor = min(melhor_cada)
            if voltas[i][j] == melhor:
                return (i-1, voltas[i][j], j-1)