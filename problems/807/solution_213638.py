def conta_frases(texto):
    '''conta o número de frases que aparecem no texto. string->int'''
    x=str.count(texto, '.')
    y=str.count(texto, '!')
    z=str.count(texto, '?')
    w=str.count(texto, '...')
    return x+y+z-2*w