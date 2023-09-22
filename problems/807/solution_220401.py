def conta_frases(f):
    a = f.count('...')
    b = f.count('.')
    c = f.count('!')
    d = f.count('?')
    if '...' in f:
        return a + b + c + d - (a * 3)
    return a + b + c + d