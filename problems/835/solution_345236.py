def melhor_volta(m):
    '''
    Esta função recebe uma matriz 6 x 10 onde cada lista é um corredor, cada elemento da lista é o tempo que o corredor
    levou para dar uma volta e a ordem dos tempos nas listas é correspondente à que volta aquele tempo foi executado
    (i.e. se 55 está na segunda posição da terceira lista, indices 1 e 2 respectivamente, a segunda 
    volta foi realizada em 55s).
    Retorna uma tupla contendo de quem foi a melhor volta, com qual tempo foi executada e que volta.
    
    Parametros
    ----------
    m (list) : matriz 6 x 10
    '''
	mi = min([j for i in m for j in i])
    return [(m.index(i)+1, mi, i.index(mi)+1) for i in m if mi in i][0]