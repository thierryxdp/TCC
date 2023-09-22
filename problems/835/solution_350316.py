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
	lista.sort()
    menor_tempo = lista[0]
    while k < 1:
        for linha in matriz:
        	for coluna in matriz:
            	if coluna == menor_tempo:
                	corredor = n 
                    volta = y
        	n += 1  
				y += 1
                    
                        
    return ( corredor,menor_tempo,volta)