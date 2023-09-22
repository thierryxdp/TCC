def repetidos(lista):
    '''Entre com uma lista para saber a quantidade de numeros que é igual ao seu
    ao seu anterior
    Lista -> Int'''
    Nlista=lista.split(", ")
    i=1
    ant=0
    c=0
    
    while i<len(lista):
        if Nlista[i]==Nlista[ant]:
            c=c+1
            ant=ant+1
        i=i+1
    
    return c