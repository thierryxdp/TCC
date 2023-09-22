def uppCons(frase):
    frase=0
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i]=frase.upper(i)
        i=i+1
    return frase