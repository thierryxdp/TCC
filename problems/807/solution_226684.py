def conta_frases(texto):
    '''Retorna o numero de frases que aparecem no texto;
    str->int'''
    a=str.count(texto,'.')
    b=str.count(texto,'...')
    c=str.count(texto,'?')
    d=str.count(texto,'!')
    return (a-2*b)+c+d