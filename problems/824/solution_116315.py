def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in "AEIOUaeiou":
            nova=frase[i].upper()
        i=i+1
    return nova