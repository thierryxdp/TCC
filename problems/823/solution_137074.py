def faltante(lista):
    ''' '''
    '''list -> int'''
    
    i=0
    peca=1
    while i <= len(lista):
        if lista[i] != peca:
            
            i=i+1
            peca=peca+1
            
        return peca