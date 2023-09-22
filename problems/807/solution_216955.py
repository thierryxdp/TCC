def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    x=frase.count("!")
    z=frase.count("?")
    w=frase.count(".")
    
    return (x+z+w)