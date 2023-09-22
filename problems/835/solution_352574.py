def melhor_volta(A):
    '''
    	A função recebe uma matriz numérica A 6x10. Nesse caso, cada elemento da 
        matriz A representa o tempo de uma volta de uma corrida de Kart, cada linha
        contém os tempos de um corredor nas 10  voltas em ordem (Ex. o elemento da 
        linha 0 e coluna 0 da matriz A contém o tempo do primeiro corredor na sua 
        primeira volta). Com isso, a matriz retorna uma tupla contendo o corredor
        com melhor tempo, o melhor tempo e a volta do melhor tempo.
        A -> list (matriz númerica 6x10)
        list -> tuple
    '''
    a = []
    for i in range(len(A)):
        a += [min(A[i])]
    melhor_t = min(a)
    corredor = a.index(melhor_t)+1 #soma-se 1 pois não há corredor 0
    volta = A[corredor-1].index(melhor_t)+1 #nem volta 0
    return (corredor,melhor_t,volta)