def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frases
    p=str.count(x,'.')
    l= str.count(x,'!')
    j= str.count(x,'?')
    k=str.count(x,'...')
    
    if p>5:
        return (p-)+l+j+k
    if p==6:
        return (p-4)+l+j+k
    if p<4:
        return p+l+j+k