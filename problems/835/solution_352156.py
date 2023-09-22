def melhor_volta(matriz):
    '''
    	Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e
        retorna uma tupla informando quem foi a melhor volta da prova, com qual tempo e em que volta.
        list -> tuple
    '''
    menores_voltas = []
    dicio = {}
    for i in range(0,len(matriz)):
        dicio.update({i:min(matriz[i])})
    return dicio
    	
    '''
    	for j in range(0,len(matriz[0]))
        	menores_voltas.append()
    '''