def conta_frases(texto):
    '''retorna o numero de frases que aparecem no texto dado'''
    '''str -> int'''
    
    a=str.count(texto,'.')
    b=str.count(texto,'!')
    c=str.count(texto,'?')
    
    
    return a+b+c