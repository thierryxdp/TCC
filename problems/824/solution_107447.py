def uppCons(frase):
    i=0
    frase=[i]
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i]=frase[i].upper()
        i=i+1
    return frase