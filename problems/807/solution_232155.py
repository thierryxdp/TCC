def conta_frases(S):
    p=str.count(S, '.',1)
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, '...')
    
    f=p+e+i+r
    
    return f