def conta_frases(x):
    
    contador = 0
    for i, termo in enumerate(x):
        if termo in ('!', '?'):
            contador += 1
        
        elif termo == '.':
            if x[i] == x[i+1] and x[i+1] == x[i+2]:
                contador += 1
            
            else:
                contador += 1
    
    return contador