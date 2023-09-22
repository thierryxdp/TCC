def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    y=0
    
    a=str.index(str, "...", 0,-1)
    
    if a>0:
        str.replace("...", "")
        y+=1
    
    else:
        
    x=str.count('!')
    
    z=str.count('?')
    
    w=str.count('.')
    
    return (x+y+z)