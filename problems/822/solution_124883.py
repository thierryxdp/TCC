def repetidos(lista):
    """recebe uma lista e retorna os numeros repetidos 
    list->int"""
    
    i=1 
    i2=0
    ac=0
    while i<len(lista):
        if lista[i] == lista[i2]:
            ac=ac+1
        i= i+1
        i2= i2+1
            
    return ac