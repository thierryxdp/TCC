def melhor_volta(m):
    '''Recebe como entrada uma matriz 6 x 10 com os tempos em segundos
    dos corredores em cada volta e retorna uma tupla informando: De
    quem foi a melhor volta da prova, com qual tempo e em que volta
    list->tuple '''
	
    melhor=[]
    
    for i in range(len(m)):
        melhor.append(min(m[i]))
   
	return melhor.index(min(melhor))+1,min(melhor),m[melhor.index(min(melhor))].index(min(melhor))+1