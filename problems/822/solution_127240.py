def repetidos(l):
    '''
    	A função recebe uma lista numérica e retorna a quantidade de vezes que um
        elemento da lista é igual ao anterior.
        l -> list (numérica)
        list -> int
    '''
    i = 0
    c = 0
    while i < len(l):
        if l[i] == l[i-1]:
            c += 1
        i += 1
    return c