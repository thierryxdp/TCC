def conta_frases(x):
    
    contador = 0
    for i, termo in enumerate(x):
        if termo in ('!', '?'):
            contador += 1
        
        elif termo == '.':
            if x[len(x)-1] == '.':
                if x[len(x)-1] == x[len(x)-2] and x[len(x)-1] == x[len(x)-3]:
                    contador += 1
            elif x[i+1] == ' ':
                contador += 1
            
          	elif x[i+1] == '.':
            	contador += 1
    
    return contador