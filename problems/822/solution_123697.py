def repetidos(lista):
    '''Entre com uma lista para saber a quantidade de numeros que é igual ao seu
    ao seu anterior
    Lista -> Int'''
    
    i=1
    c=0
    ant=0
    
    while i<len(lista):
        if lista[i]==lista[i-1]:
            c=c+1
        i=i+1
    
    return c