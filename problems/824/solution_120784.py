def uppCons(frase):
    frase=list(frase)
    for f in range(len(frase)):
        if frase[f] not in "aeiouAEIOU":
            frase[f]= frase[f].upper()
    frase="".join(frase)
    return frase