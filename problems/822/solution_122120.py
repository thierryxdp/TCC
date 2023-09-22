def repetidos(lista):
    a=len(lista)-1
    b=0
    c=0
    proximo = 0
    while proximo < a:
        if lista[b] == lista[b+1]:
            c=c+1
        proximo = proximo + 1
        b=b+1
    return c