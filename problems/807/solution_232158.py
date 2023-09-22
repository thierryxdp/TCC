def conta_frases(S):
    p=str.count(S, '.')
    e=str.count(S, '!')
    i=str.count(S, '?')
    r=str.count(S, r'...')
    
    f=p+e+i+r
    
    return f