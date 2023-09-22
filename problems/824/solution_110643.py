def uppCons(frase):
    prox=0
    final=''
    while prox<len(frase):
        if frase[prox] != 'AEIOUaeiou':
            frase = frase[lower.prox]
        prox=prox+1
    return frase