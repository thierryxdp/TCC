def conta_frases(x):
    '''Esta função conta o número de frases que aparecem no texto
    assinatura str -> int'''
    a=str.count(x,'!')+str.count(x,'?')
    b=str.count(x,'...')
    c=str.count(x,'.')
    d=c-(3*b)
    return a+b+d