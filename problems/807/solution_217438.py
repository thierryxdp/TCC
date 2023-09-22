def conta_frases(s):
    f = s.count('.')
    if f > 1:
        f = 1
    n = f + s.count('!') + s.count('?')
    if n == 1 and (s[-1] == '.' or '!' or '?' or '...'):
        return 1
    elif n == 1:
        return 2
    else:
        return n