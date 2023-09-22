def faltante (lista):
    '''
    	essa função serve para identificar qual número está faltando em uma lista de inteiros
        de tamanho não específico
        list->int
    '''
    i = 0
    while i+1 < len(lista):
        if lista[i] +1 != lista[i]+1 :
            return lista[i]+1
        i=i+1
    return lista[i]+1