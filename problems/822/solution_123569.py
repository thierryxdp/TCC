def repetidos(lista):
    '''Entre com uma lista para saber a quantidade de numeros que é igual ao seu
    interior
    Lista -> Int'''
    i=1
    c=0
    ant=0

    while i<len(lista):
        if lista[i]==lista[ant]:
            c=c+1
            ant=ant+1
    i=i+1

    return c