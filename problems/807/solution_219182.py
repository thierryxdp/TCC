def conta_frases(texto):
    '''Calcula e retorna o numero de frases em um texto,
       dado como valor de entrada;
       str -> int'''
    ind = 0
    
    lista = []
    
    for n in texto:
        
        if n == '.' and ind != len(texto) - 1:
            
            if texto[ind+1] == '.':
                
                lista.append(texto[:ind+3])
                
            else:
                
                lista.append(texto[:ind+1])
        
        elif n == '.' and ind == len(texto) - 1:
            
            lista.append(texto[:ind+1])
             
        elif n == '?' or n == '!':
            
            lista.append(texto[:ind+1])
            
        ind += 1
        
    return len(lista)