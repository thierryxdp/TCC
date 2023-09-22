def conta_frases(frase):
    """calculo e retorno da funcao que conta o numero de frases que aparecem no texto"""
    x=frase
    p=str.count(x,'.')
    l=str.count(x,'!')
    j=str.count(x,'?')
    k=str.count(x,'...')
    if '...'==1:
        return p+l+j+k