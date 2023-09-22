def repetidos(lista):
    '''função em que dada uma lista de números, retorna
    o número de vezes que um elemento da lista é igual
    ao elemento anterior; list -> list'''
    dup=0
    i=0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            dup= dup+1
        i = i+1
    return dup