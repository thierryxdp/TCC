def filtraMultiplos(l_numeros,n):
    '''
    	A função recebe uma lista numérica e um número n; com isso retorna uma nova 
        lista contendo apenas os elementos da lista inicial múltiplos de n.
        l_numeros -> list (lista numerica)
        n -> float
        list, float -> list
    '''
    i = 0
    l_multiplos = []
    while i < len(l_numeros):
        if l_numeros[i] % n == 0:
            l_multiplos += list(l_numeros[i])
        i += 1
    return l_multiplos