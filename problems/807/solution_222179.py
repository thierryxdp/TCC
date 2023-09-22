def conta_frases(texto):
    """ Função que conta quantas frases existem num determinado texto
    str -> int """
    x=str.count(texto,'...')
    y=str.count(texto,'.')-(3*x)
    z=str.count(texto,'!')
    w=str.count(texto,'?')
    return x+y+z+w