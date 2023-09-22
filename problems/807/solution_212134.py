def conta_frases(s):
    sn=s.replace('...','.')
    a=sn.count('.')
    b=sn.count('!')
    c=sn.count('?')
    return a+b+c