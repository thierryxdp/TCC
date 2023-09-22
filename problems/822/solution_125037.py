def repetidos(l):
    '''Recebe uma lista de numeros e retorna o numero de
    vezes que um elemento da lista eh igual ao elemento
    anterior; list -> int'''
    i=0
    c=0
    while i<len(l):
        if l[i]==l[(i-1)]:
            c+=1
        i += 1
    return c