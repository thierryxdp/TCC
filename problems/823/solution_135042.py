def faltante(lista):
    '''informa o numero que esta faltando na ordem da lista dada
       list -> int'''
    
    a=len(lista)
    b=0
    c=1
    d=0
    
    while b<a:
        if lista[b]==c:
            b=b+1
            c=c+1
        else:
            d=c
    return d