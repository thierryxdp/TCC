def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    y=frase.replace("...", "")
    x=y.count('!')
    z=x.count('?')
    w=z.count('.')
    
    return w