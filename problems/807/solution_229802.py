def conta_frases(x):
    '''função que conta o número de frases que aparecem no texto, segundo as
    pontuações ali presentes'''
    a=str.count(x,'!')+str.count(x,'?')
    b=str.count(x,'...')
    c=str.count(x,'.')
    d=c-(3*b)
    return a+b+d