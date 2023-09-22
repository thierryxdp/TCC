def uppCons(frase):
    i=0
    k=len(frase)
    while i < k:
        if frase[i] not in 'AEIOUaeiou':
            frase[i]=frase.upper(i)
        i=i+1
    return frase