def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    a=frase
    
    if a.count("...") == True:
        b=a.count("...")
        y=a.replace("...", "")
        
    elif a.count("!") == True:
        c=a.count("!")
    
    elif a.count("?") == True:
        d=a.count("?")
    
    elif a.count(".") == True:
        e=a.count(".")
        
    return (b+c+d+e)