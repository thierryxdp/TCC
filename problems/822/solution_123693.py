def repetidos(lista):
    '''Entre com uma lista para saber a quantidade de numeros que é igual ao seu
    ao seu anterior
    Lista -> Int'''
   
    i=1
    ant=0
    c=0
    
    while i<len(lista):
        x=lista[i]
        y=lista[ant]
        
        if x==y:
            c=c+1
            ant=ant+1
        i=i+1
    
    return c