def conta_frases(texto):
    '''retorna o numero de frases que aparecem no texto dado'''
    '''str -> int'''
    
    a=str.count(texto,'.',[0],[1])
    b=str.count(texto,'!')
    c=str.count(texto,'?')
    d=str.count(
    return a+b+c