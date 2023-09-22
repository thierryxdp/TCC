def conta_frases(texto):
    
    cont = 0    
    cont += texto.count('?', 0, len(texto))
    cont += texto.count('!', 0, len(texto))    
     
    index = texto.index('.')
  
    if texto[index+1] == '.':
        cont += 1
        
    else:
        cont += texto.count('.', 0, len(texto))
        
    
    return cont