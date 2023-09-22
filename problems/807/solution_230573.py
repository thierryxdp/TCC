def conta_frases(x):
    a=str.count(x,'.')
    b=str.count(x,'...')
    c=str.count(x,'!')
    d=str.count(x,'?')
    k=a+b+c+d
    return k-3*b