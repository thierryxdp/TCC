def melhor_volta(matriz):
    '''Dada como entrada uma matriz 6x10
    com os tempos em segundos dos corredores
    de cada volta, retorna quem foi a melhor
    volta da prova, com qual tempo e em que 
    volta
    list -> tuple'''
    n = 1
    k = 1
    y = 1
    volta = 0
    corredor = 0
    lista = []
    for linha in matriz:
        for coluna in matriz:
            lista.append(coluna)
    menor_tempo = lista.min
    while k < 1:
        for linha in matriz:
        	for coluna in matriz:
            	if coluna == menor_tempo:
                	corredor = n 
                    
        	n += 1  
				
	return ( corredor,menor_tempo)