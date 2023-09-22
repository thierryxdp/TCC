def conta_frases(s):
    a=s.count('.')
    b=s.count('!')
    c=s.count('?')
    d=s.count('...')==1
    return a+b+c+1