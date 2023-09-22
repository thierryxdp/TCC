def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    y=frase.replace("...","")
    x=frase.count("!")
    z=frase.count("?")
    w=frase.count(".")
    
    a = (len(y)-1)
    
    return (x+z+w+a)