def conta_frases(F):
    x0 = F.split('.')
    x1 = x0.split('!')
    x2 = x1.split('?')
    x3 = x2.split('...')
    return len(x3)