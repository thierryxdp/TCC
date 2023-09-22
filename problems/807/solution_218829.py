def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    b=len(frase)
    
    y=frase.count("...")
    x=frase.count('!')
    z=frase.count('?')
    w=frase.count('.')
    
    return (x+y+z)-((y*3)-w)