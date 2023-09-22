def melhor_volta(matriz):
    '''
    	Função que recebe uma matriz 6 x 10
        com os tempos dos competidores em 
        cada volta, e retorna uma tupla com
        o competidor da melhor volta, o tempo
        dessa volta e a própria volta
        : param matriz: list(list)
        : return: tuple
    '''
    num_compet = len(matriz)
    num_voltas = len(matriz[0])
    melhores_tempos = []
    melhores_voltas = []
    
    for competidor in range(num_compet):
        melhor_tempo = matriz[competidor][0]
        contador_volta = 0
        melhor_volta = contador_volta
        for volta in range(num_voltas):
            if matriz[competidor][volta] < melhor_tempo:
                melhor_tempo = matriz[competidor][volta]
                melhor_volta = contador_volta
            contador_volta += 1
        list.append(melhores_tempos,melhor_tempo)
        list.append(melhores_voltas,melhor_volta)
        
    melhor_tempo_total = min(melhores_tempos)
    compet = list.index(melhores_tempos,melhor_tempo_total)
    melhor_volta_total = melhores_voltas[compet]
    
    compet += 1
    melhor_volta_total += 1
    
    return compet,melhor_tempo_total,melhor_volta_total