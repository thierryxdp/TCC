def faltante(lista):
    '''retorna o numero faltante na lista dada'''
    '''list -> int'''
    
    cont = 0
    falt = 0
    
    while cont <= len(lista):
        
        falt = falt+lista[cont]
        cont = cont + 1
        
    return falt