def melhor_volta(m):
    '''
    	 essa função recebe uma matriz 6x10 com os tempos em segundos de cada competidor
         em cada volta e retorna uma tupla que informa de quem foi a melhor volta da corrida,
         com qual tempo e em qual volta foi.
         list -> tuple
    '''
    x = ()
    len(m) = 6
    len(m[0]) = 10
    matriz = []
    for r in range(6):
        linha = []
        for c in range(10):
            linha.append(x.randint(10, 99))
        matriz.append(linha);
    return (matriz)