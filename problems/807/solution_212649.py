def conta_frases(frases):
    """calculo e retorno de uma funcao que conte o numero de frases que aparecem no texto."""
    x= frases
    p=str.count(x,'.')
    l= str.count(x,'!')
    k =str.count(x,'...')
    return (p+l+k)/2