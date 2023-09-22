def conta_frases(texto):
    '''Função que conta o numero de frase em um texto dado.
    str->int'''
    
    a=str.count(texto,'!')
    b=str.count(texto,'?')
    c=str.count(texto,'.')
    d=str.count(texto,'. ')
    import math
    e= math.ceil(c/3)
    if c<3:
        return a+b+c+d
    else:
        a+b+d+e