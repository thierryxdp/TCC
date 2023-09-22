def uppCons(frase):
    frase= tupple(frase)
    frase_cons= ()
    i= 0
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxz":
            frase_cons= frase_cons + (frase[i].upper(),)
        else:
            frase_cons= frase_cons + (frase[i],)
        i=i+1
    return list(frase_cons)