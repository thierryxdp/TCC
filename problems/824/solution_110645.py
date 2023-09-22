def uppCons(frase):
    prox=0
    final=''
    while prox<len(frase):
        if frase[prox] != 'AEIOUaeiou':
            frase = upper(frase[prox])
        prox=prox+1
    return frase