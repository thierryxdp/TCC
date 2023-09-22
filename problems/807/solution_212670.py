def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frases
    p=str.count(x,'.')
    l= str.count(x,'!')
    k =str.count(x,'...')
    if '.'!='...':
        return p+l+k