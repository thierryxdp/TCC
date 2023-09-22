def conta_frases(S):
    p=str.index(S, '.')
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, '...')
    
    f=p+e+i+r
    
    return f