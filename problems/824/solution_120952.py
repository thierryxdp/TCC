def uppCons(frase):
    lista=list(frase)
    i=0
    while i<len(lista):
        if lista[i] in "bcdfghjklmnpqrstvwxyz":
            str.upper(lista[i])
        i=i+1
    return frase