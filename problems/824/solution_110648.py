def uppCons(frase):
    prox=0
    while prox<len(frase):
        if frase[prox] != 'AEIOUaeiou':
            frase = frase.upper
        prox=prox+1
    return frase