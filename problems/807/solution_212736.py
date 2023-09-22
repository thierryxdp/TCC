def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frases
    x=frases
    p=str.count(x,'.')
    l= str.count(x,'!')
    k =str.count(x,'...')
    j= str.count(x,'?')
    g=p+l+j+k

    if p>4:
        return g-2
    if p>6:
        return g-3