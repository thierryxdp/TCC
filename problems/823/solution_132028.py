def faltante(L):
    '''Esta função retorna o número faltante na lista (L)
    inserida.
    list -> int'''
    
    indice=0
    sucessor=1
    
    list.sort(L)
    
    while sucessor<len(L):
        if L[sucessor]-L[indice]!=1:
            falta=L[indice]+1
            
        elif L[indice]!=1:
            falta=1
   		
        indice=indice+1
        sucessor=sucessor+1
        
    return falta