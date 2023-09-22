def melhor_volta(matriz):
    '''Essa função retorna de quem foi a melhor volta numa pista de 
    kart, com qual tempo e em que volta.
    list >>> list '''
    vencedor = 0
    tempo = 0
    volta = 0
    lista = []
    
   melhor_tempo = matriz[0][0]
    for i in range(len(matriz)):
        tempo_corredor = min(matriz[i])
        if tempo_corredor < melhor_tempo:
            melhor_tempo = tempo_corredor
            melhor_corredor = i
	volta = list.index(matriz[melhor_corredor], melhor_tempo)
    
    return volta