def filtraMultiplos(lista,n):
    ''' funçao filtra os numeros multiplos de um numero n'''
    '''list --> list'''
    
    l=[]
    i=0
    while i < len(lista):
        if lista[i]%n==0:
            l= l + [lista[i],]
        i = i + 1
    return l