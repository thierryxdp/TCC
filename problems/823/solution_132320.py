def faltante(L):
    '''Esta função retorna o número faltante na lista (L)
    inserida.
    list -> int'''
    
    indice=0
    sucessor=1
    
      
    list.sort(L)
    
    while sucessor<len(L)-1:
        if L[sucessor]-L[indice]!=1:
            falta=falta+L[indice]
           		
        indice=indice+1
        sucessor=sucessor+1
        
    if L[0]!=1:
        return 1
        
    return falta