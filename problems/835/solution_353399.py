def melhor_volta(matriz):
    '''Essa função retorna de quem foi a melhor volta numa pista de 
    kart, com qual tempo e em que volta.
    list >>> list '''
    vencedor = 0
    tempo = 0
    volta = 0
    lista = []
    
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            lista += [matriz[i][j]]
    
    tempo = min (lista)
    
    
   	for i in range(len(matriz)):
        tempos_corredor = matriz[i]
        if tempo in tempos_corredor:
            vencedor = i
	
    volta = list.index(matriz[vencedor], tempo)
    
    return vencedor, tempo, volta