def uppCons(frase):
    frase= list(frase)
    frase_cons= []
    i= 0
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxzç":
            frase_cons.append(frase[i].upper())
        else:
            frase_cons.append(frase[i])
        i=i+1
    return ''.join(frase_cons)