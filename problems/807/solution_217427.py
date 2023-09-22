def conta_frases(s):
    n = s.count('.') + s.count('!') + s.count('?') + s.count('...')
    if n == 1:
        return 2
    else:
        return n