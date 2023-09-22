def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''

    x=0
    
    y=str.count('!')
    x=x+y
    
    z=str.count('.')
    x=x+z
    
    w=str.count('?')
    x=x+w
    
    #v=str.count("...")
    #x=x+v

    return x