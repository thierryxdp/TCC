def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in frase[1]:
            frase=frase.replace(frase[1],frase[i].upper())
        i=i+1
    return frase