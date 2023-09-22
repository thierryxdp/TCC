def melhor_volta(A):
    '''
    	A função recebe uma matriz numérica A 6x10 e retorna a linha +1 que contem
        o menor número, esse número e a coluna +1 que contem esse número em uma
        tupla. Nesse caso, cada elemento da matriz A representa o tempo de uma volta
        de uma corrida de Kart feita por um corredor, cada linha contém os tempos de
        um corredor nas 10 voltas.
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