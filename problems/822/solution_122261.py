def repetidos(n):
    '''Dado uma lista de números n, retorne o número de vezes que o elemento da lista é igual o elemento anterior;
    list->int'''
    i=0
    c=0
    while i<len(n):
        if n[i]==n[i-1]:
            c=c+1
        i=i+1
    return c