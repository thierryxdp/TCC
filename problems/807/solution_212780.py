def conta_frases(frases):
    """calculo e retorno de uma funcao que conta o numero de frases que aparecem em um texto"""
    x=frase
    p=str.count(x,'.')
    l= str.count(x,'!')
    j= str.count(x,'?')
    if p>5:
        return (p-2)+l+j
    if p==6:
        return (p-4)+l+j
    if p<3:
        return p+l+j