def faltante(lista):
    ''' '''
    '''list -> int'''
    
    i=0
    peca=1
    tamanho_lista=len(lista)
    
    while i <= tamanho_lista:
        if tamanho_lista != tamanho_lista+1 and peca not in lista :
            i=i+1
            peca=peca+1
            
    return peca