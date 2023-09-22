def conta_frases(x):
    if '.' in x:
        return 1
    if '.' and '!' in x:
        return 2
    if '.' and '!' and '...' in x:
        return 3
    if '.' and '!' and '...' and '?' in x:
        return 4
    if '!' in x:
        return 1
    if '!' and '...' in x:
        return 2
    if '!' and '?' in x:
        return 2