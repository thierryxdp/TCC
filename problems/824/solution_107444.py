def uppCons(frase):
    frase=[]
    i=0
    k=len(frase)
    while i < k:
        if frase[i] not in 'AEIOUaeiou':
            frase[i]=frase[i].upper()
        i=i+1
    return frase