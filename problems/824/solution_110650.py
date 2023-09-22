def uppCons(frase):
    prox=0
    while prox<len(frase):
        if frase[prox] != 'AEIOUaeiou':
            frase = str.replace(frase,frase[prox],str.upper(frase[prox]))
        prox=prox+1
    return frase