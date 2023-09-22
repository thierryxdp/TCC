def posLetra(texto,letra,numero):
    
    posicao = ()
    
    i = 0
    
    while i < len (texto):
        
        if texto[i] == letra:
            posicao = i
            
                       
        i = i + 1
          
    return posicao