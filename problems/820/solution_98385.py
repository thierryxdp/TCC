def posLetra(frase,letra,oc):
    '''Recebe uma frase, uma letra e uma ocorrência e retorna 
       a posição da ocorrência da letra dada na frase;
       str, str, int -> int'''
    
    pos = -1
    meta = 0
    
    while meta != oc:
        
        pos += 1
        
        if frase[pos] == letra:
            
            meta += 1
    
    if meta == 0:
        
        return -1
    
    else:
        
        return pos