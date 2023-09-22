def conta_frases(texto):
    '''Calcula e retorna o numero de frases em um texto,
       dado como valor de entrada;
       str -> int'''
    
    contagem = 0
    
    ind = 0
    
    for n in texto:
        
        if n == '.':
            
            if texto[ind-1] == '.':
                
                pass
                
            else:
                
                contagem += 1
        
        elif n == '?' or n == '!':
            
            contagem += 1
            
        ind += 1
        
    return contagem