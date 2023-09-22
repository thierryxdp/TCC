def conta_frases(S):
    p=str.count(S, '.')
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, '...')-3
    
    f=p+e+i+r
    
    return f