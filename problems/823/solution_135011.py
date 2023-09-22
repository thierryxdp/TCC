def faltante (lista):
    '''
    	essa função serve para identificar qual número está faltando em uma lista de inteiros
        de tamanho não específico
        list->int
    '''
    i = 0
    if 1 not in lista:
        return 1
    if 2 not in lista: 
        return 2
    if 3 not in lista:
        return 3
    if 4 not in lista:
        return 4
    if 5 not in lista: 
        return 6
    if 6 not in lista:
        return 6
    while i+1 < len(lista):
        if lista[i] +1 != lista[i]+1 :
            return lista[i]+1
        i=i+1
    return lista[-1]+1