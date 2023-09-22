def conta_frase(x):
    a=str.count(x,'!')+str.count(x,'?')
    b=str.count(x,'...')
    c=str.count(x,'.')
    d=c-(3*b)
    return a+b+d