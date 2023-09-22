def melhor_volta(voltas):
    '''identifica qual foi a melhor volta, o tempo dela e o corredor que a 
    realizou numa corrida'''
    melhor = min(voltas)
    tupla = ()
    for i in range(0, 6):
        for j in range(0, 10):
            if voltas[i][j] == melhor:
                tupla += (i, voltas[i][j], j)
	return tupla