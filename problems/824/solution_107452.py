def uppCons(frase):
    i=0
    frase=[]
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i]=frase.upper(i)
            i=i+1
    return frase