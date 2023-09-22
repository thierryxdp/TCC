def conta_frases(texto):
    ''' '''
    a=str.count(texto,'.')
    b=str.count(texto,'...')
    c=str.count(texto,'?')
    d=str.count(texto,'!')
    
    if a and b in texto:
        return a+b+c+d-(a+b-2)
    else:
        return a+b+c+d