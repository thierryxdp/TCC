def conta_frases(n):
    A = list(n)
    B = list.count(A,'.')
    C = list.count(A,'!')
    D = list.count(A,'?')
    E = list.count(A,'...')
    return A + B + C + D