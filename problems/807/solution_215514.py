def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    x=str.index('!')
    
    y=str.index('...')
    
    z=str.index('?')
    
    w=str.index('.')
    
    return (x+y+z+w)