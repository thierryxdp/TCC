def conta_frases(texto):
    """
    conta o numero de frases em um texto
    strint->string
    """
    a=str.count(texto,'.')
    b=str.count(texto,'...')
    c=str.count(texto,'!')
    d=c-(3*b)
    e=str.count(texto,'?')
    return a+b+c+d+e