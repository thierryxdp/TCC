def repetidos(lista):
    n=0
    m=0
    l=(n+1)
    while n <((len(lista))-1):
        if lista[n] == lista[l]:
            n = n + 1
        n=n+1
        l=(n+1)        
    return n