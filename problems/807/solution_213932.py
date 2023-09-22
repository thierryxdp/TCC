def conta_frases(texto):
    
    cont = 0
    index1 = texto.index('.')
    index2 = texto.index('?')
    index3 = texto.index('!')
    
  
    if texto[index1+1] == '.':
        cont += texto.count('...', 0, len(texto))
    
    
    if texto[index2] == '?':
        cont += 1
    
    if texto[index3] == '!':
        cont += 1  
        
        
    cont += texto.count('.', 0, len(texto))
    
    return cont