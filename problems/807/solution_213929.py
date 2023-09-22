def conta_frases(texto):
    
    cont = 0
    index = texto.index('.')    
  
    if texto[index+1] == '.':
        cont += texto.count('...', 0, len(texto))
    
    
    if texto[-1] == '?':
        cont += 1
    
    if texto[-1] == '!':
        cont += 1  
        
    if texto[index+1] == '.':
        cont += texto.count('.', 0, len(texto))
    
    return cont