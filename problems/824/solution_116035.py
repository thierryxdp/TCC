def uppCons(frase):
    consoante='bcçdfghjklmnpqrstvxwyz'
    j=0
    while j<len(frase):
        if j in consoante:
            frase.upper()
        j=j+1
    return frase