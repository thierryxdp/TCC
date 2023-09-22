def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    i=0
    recip=0
    
    while i< len(lista):
        
        recip=recip+lista[i]
        i=i+1
        
    return recip