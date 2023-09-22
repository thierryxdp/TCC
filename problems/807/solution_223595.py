def conta_frases(n):
    """Dada uma str n, conta o números de frases nela contida
    str->int"""
    L = list(n)
    A = list.count(L,'.')
    B = list.count(L,'!')
    C = list.count(L,'?')
    D = list.count(L,'...')
    return A + B + C + D