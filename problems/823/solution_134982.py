def faltante (lista):
    '''
    	essa função serve para identificar qual número está faltando em uma lista de inteiros
        de tamanho não específico
        list->int
    '''
    i = 0
    x = 0
    if 1 not in lista:
        return 1
    while i+1 < len(lista):
        if x[i] +1 != x[i]+1 :
            return lista[i]+1
        i=i+1
    return lista[-1]+1