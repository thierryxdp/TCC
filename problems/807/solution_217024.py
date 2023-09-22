def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    a=frase
    
    if a.count("...") == True:
        y1=a.count("...")
        y=a.replace("...", "")
        
    elif a.count("!") == True:
        x1=a.count("!")
    
    elif a.count("?") == True:
        w1=a.count("?")
    
    elif a.count(".") == True:
        z1=a.count(".")
    
    else:
        return "Frase Invalida"
    
    return (y1+x1+w1+z1)