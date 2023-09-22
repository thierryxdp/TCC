def conta_frases(x):
    a=str.count(x,'. ')
    c=str.count(x,'!')
    d=str.count(x,'?')
    k=a+c+d
    if a>1:
        return k+1
    return k