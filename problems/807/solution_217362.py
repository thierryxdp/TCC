def conta_frases(s):
    n = []
    n = n + s.split('.')
    n = n + s.split('!')
    n = n + s.split('?')
    n = n + s.split('...')
    return len(n)