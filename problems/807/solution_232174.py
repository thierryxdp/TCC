def conta_frases(S):
    p=str.count(S, '.')
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, '...')
    
    c=i-(r*3)
    
    f=p+e+c+r
    
    return f