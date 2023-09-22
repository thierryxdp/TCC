def melhor_volta(m):
    '''
    	 essa função recebe uma matriz 6x10 com os tempos em segundos de cada competidor
         em cada volta e retorna uma tupla que informa de quem foi a melhor volta da corrida,
         com qual tempo e em qual volta foi.
         list -> tuple
    '''
    nLinha = 6
    nColuna = 10
    menor = m[0][0]
    for i in range(6):
        linha = m[1]
        for j in linha:
            menor = j if menor > j else menor
    return menor