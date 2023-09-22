def repetidos(x):
    '''Retorna o número de vezes que um elemento da lista é igual ao anterior.
    list -> int'''
    i=0
    a=0
    while i<len(x):
        if x[i]=x[i+1]:
            a=a+1
            i=i+1
        else:
            i=i+1
    return a