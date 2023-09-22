def conta_frases(texto):
    
    cont = 0
    cont += texto.count('.', 0, -1)
    #cont += texto.count('...', 0, -1)
    
    #if texto[-1] == '?':
     #   cont += 1
    
    #if texto[-1] == '!':
     #   cont += 1  
    
    return cont