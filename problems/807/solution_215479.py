def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''

    x=0
    
    y=str.index(frase,'!')
    x+=y
    z=str.index(frase,'.')
    x+=z
    w=str.index(frase,'?')
    x+=w
    v=str.index(frase,'...')
    x+=v
    
    return x