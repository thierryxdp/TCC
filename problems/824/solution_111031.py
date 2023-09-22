def uppCons(frase):
    frase= list(frase)
    frase_cons= []
    i= 0
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxz":
            frase_cons.append(frase[i].upper())
        else:
            frase_cons.append(frase[i])
        i=i+1
    return frase_cons[]