def melhor_volta(m):
    '''
    	 essa função recebe uma matriz 6x10 com os tempos em segundos de cada competidor
         em cada volta e retorna uma tupla que informa de quem foi a melhor volta da corrida,
         com qual tempo e em qual volta foi.
         list -> tuple
    '''
    melhor = []
    for i in range(6):
        linha = []
        for j in range(10):
            linha.append((m[i]+m[j]))
        melhor.append(linha)    
    return melhor