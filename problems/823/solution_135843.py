def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    ultimo=lista[-1]
    
    falt=ultimo*(1+ultimo)/2
    
    return falt