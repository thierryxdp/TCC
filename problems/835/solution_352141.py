def melhor_volta(matriz):
    '''
    	Funcao recebe um matriz 6 x 10 com os tempos
        em segundos dos corredores em cada volta, 
        e retorna uma tupla informando de quem foi a
        melhor volta da prova, com qual tempo e em que volta.
        list -> tuple
        
    '''
    
    melhores_tempos = []
    for i in range(len(matriz)):
        list.append(melhores_tempos, min(matriz[i]))
    melhor_tempo = min(tuple(melhores_tempos))
    melhor_corredor = list.index(melhores_tempos,melhor_tempo)+1
    melhor_volta = list.index(matriz[melhor_corredor-1],melhor_tempo)+1
    return (melhor_corredor,melhor_tempo,melhor_volta)