def conta_frases(x):
    ponto=x.count('.')
    interrog=x.count('?')
    exc=x.count('!')
    retcs=x.count('...')
    if ponto>4:
        x=x-3
        
    x=ponto+interrog+exc+retcs
    return x