def repetidos(l):
    """retorna o numero de vezes que um elemento da lista 'l' é igual ao elemento anterior.
    list->int"""
    prox=0
    n=0
    while prox<len(l)-1:
        if l[prox]==l[prox+1]:
            n=n+1 
        prox=prox+1
    return n