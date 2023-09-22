def repetidos(lista):
    """função que vai receber uma lista e depois 
    retorna o número de vezes que um elemento dela vai 
    ser igaul ao elemento anterior list->int"""
    n=0
    m=0
    l=(n+1)
    while n <((len(lista))-1):
        if lista[n] == lista[l]:
            m= m + 1
        n=n+1
        l=(n+1)        
    return m