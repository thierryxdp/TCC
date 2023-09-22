def faltante(lista):
    '''informa o numero que esta faltando na ordem da lista dada
       list -> int'''
    
    a=len(lista)+1
    b=0
    c=1
    
    while b<a:
        if lista[b]==c:
            b=b+1
            c=c+1
        else:
            return c