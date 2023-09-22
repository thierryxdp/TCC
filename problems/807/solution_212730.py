def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frases
    if '.'+'.'+'.':
        return x-2
    if '.'>4:
        return x-2
    if '.'>6:
        return x-3
    x=frases
    p=str.count(x,'.')
    l= str.count(x,'!')
    k =str.count(x,'...')
    j= str.count(x,'?')
        return p+l+j+k