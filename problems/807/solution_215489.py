def conta_frases(str):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''

    x()
    
    y=str.count('!')
    x+=y
    z=str.count('.')
    x+=z
    w=str.count('?')
    x+=w
    v=str.count('...')
    x+=v

    return x