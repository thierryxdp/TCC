def conta_frases(texto):
    """Função que conta quantas frases há num texto.
    str->str"""
    a=str.count(texto,'!')
    b=str.count(texto,'?')
    c=str.count(texto,'.')
    d=str.count(texto,'. ')
    
    if c<3:
        return a+b+c
    else:
        return a+b+c-3+1