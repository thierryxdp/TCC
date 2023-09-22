def uppCons(frase):
    consoante='bcdfghjklmnpqrstvxwyz'
    j=0
    while j<len(frase):
        if frase[j] in consoante:
            j+=frase[j].upper()
    return frase