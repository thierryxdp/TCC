def conta_frases(s):
    a=s.count('.')
    b=s.count('!')
    c=s.count('?')
    d=s.count('...')
    if a>0 and d>0:
        return a+b+c+1
    else:
        a+b+c+d