def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    x=str.count('!')
    
    y=str.count("...")
    
    z=str.count('?')
    
    w=str.count(x,'...')
    
    return (x+y+z+w)