def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    i=0
    falt=0
    
    while i < len(lista):
        
        falt=falt+lista[i]
        i=i+1
        
    return falt