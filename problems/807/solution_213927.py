def conta_frases(texto):
    
    cont = 0
    cont += texto.count('.', 0, len(texto))
    cont += texto.count('...', 0, len(texto))
    
    if texto[-1] == '?':
        cont += 1
    
    if texto[-1] == '!':
        cont += 1  
    
    return cont