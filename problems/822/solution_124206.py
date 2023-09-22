def repetidos(x):
    '''Retorna o número de vezes que um elemento da lista é igual ao anterior.
    list -> int'''
    i=0
    a=0
    while i<len(x-1):
        b=i+1
        if x[i]==x[b]:
            a=a+1
            i=i+1
        else:
            i=i+1
    return a