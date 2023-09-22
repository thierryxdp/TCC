def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    a=frase
    
    if frase.count("...") == TRUE:
        Y1=frase.count("...")
        y=a.replace("...", "")
        
    elif a.count("!") == TRUE:
        X1=a.count("!")
    
    elif a.count("?") == TRUE:
        W1=a.count("?")
    
    elif a.count(".") == TRUE:
        Z1=a.count(".")
    
    else:
        return "Frase Invalida"
    
    return (Y1+X1+W1+Z1)