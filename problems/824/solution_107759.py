def uppCons(frase):
    i=0
    while i<=len(frase):
        if frase not in'AEIOUaeiou':
            frase=frase[i].upper()
        i=i+1
    return frase