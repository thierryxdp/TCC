def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    x=str.count('!')
    
    y=str.count('.', 1)
    
    z=str.count('?')
    
    return (x+y+z)