def melhor_volta(m):
    '''
    	 essa função recebe uma matriz 6x10 com os tempos em segundos de cada competidor
         em cada volta e retorna uma tupla que informa de quem foi a melhor volta da corrida,
         com qual tempo e em qual volta foi.
         list -> tuple
    '''
    m1 = m.index(min(m))
    m2 = m[m1].index(min(m[m1]))
    return m1, m2