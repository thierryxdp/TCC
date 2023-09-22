def conta_frases(x):
    
    contador = 0
    for i, termo in enumerate(x):
        if termo in ('!', '?'):
            contador += 1
        
        elif termo == '.':

          if x[i+1] == ' ':
            contador += 1
            
          elif x[i+1] == '.':
            contador += 1
    
    return contador