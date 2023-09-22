def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    y=frase.replace("...", "")
    x=int(y.count('!'))
    z=int(x.count('?'))
    w=int(z.count('.'))
    
    return w