def conta_frases(entrada):
    if '!' and '?' and '...' and '.' in entrada == True:
        return ((len(entrada.split('.') + entrada.split('!') + entrada.split('?') + entrada.split('...'))) - 3)/2
    else:
        return False