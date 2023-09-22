def repetidos(lista):
    n = 0
    v = 0
    c = (n+1)
    while n<((len(lista))-1):
        if lista[n] == lista[c]:
            v= v+1
            n= n+1
            c=(n+1)
            return v