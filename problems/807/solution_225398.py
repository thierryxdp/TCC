def conta_frases(entrada):
    return ((len(entrada.split('.') + entrada.split('!') + entrada.split('?') + entrada.split('...'))) - 3)/2