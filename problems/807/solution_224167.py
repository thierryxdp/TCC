def conta_frases(texto):
    '''retorna o numero de frases que aparecem no texto dado'''
    '''str -> int'''
    
    a=texto.count('.')
    b=texto.count('!')
    c=texto.count('?')
    d=texto.count('...')
    
    frases=a+b+c+d
    
    if d >= 1:
        return frases - d*3
    return frases