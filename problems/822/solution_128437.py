def repetidos(lista):
    '''retorna o número de vezes que um elemento da lsita é igual ao elemneto anterior
    list->int'''
    i=0
    n=0
    while i<len(lista):
        if lista[i-1] == lista[i]:
            n= n+1
        i = i+1
    return n