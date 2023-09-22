def uppCons(frase):
    prox = 0
    while frase[prox] < len(frase):
        if frase[prox] != 'AEIOUaeiou':
            frase[prox].upper()
        prox = prox + 1
    return frase