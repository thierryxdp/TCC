def conta_frases(s):
    a=s.count('.')
    b=s.count('!')
    c=s.count('?')
    if '...' in s:
        return a+b+c+1
    else:
        a+b+c