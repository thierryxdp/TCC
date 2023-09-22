def repetidos(lista):
    '''retorna o numero de vezes que um numero é igual ao numero anterior'''
    '''list -> int'''
    
    q=0
    i=0
    
    while i < len(lista):
        if lista[i] == lista[i+1]:
            q = q + 1  
        i = i + 1
            
    return q