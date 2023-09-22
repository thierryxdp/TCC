def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frases
    if '.' is not '...':
    p=str.count(x,'.')
    l= str.count(x,'!')
    k =str.count(x,'...')
    j= str.count(x,'?')
    return p+l+k+j