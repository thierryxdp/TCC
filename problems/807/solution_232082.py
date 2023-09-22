def conta_frases(x):
    ponto=x.count('.')
    interrog=x.count('?')
    exc=x.count('!')
    retcs=x.count(str('...'))
    x=ponto+interrog+exc+retcs
    return x