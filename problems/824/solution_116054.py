def uppCons(frase):
    consoante='bcçdfghjklmnpqrstvxwyz'
    j=0
    while j<len(frase):
        if frase[j] in consoante:
            frase=str.replace(frase[j],frase[j].upper())
            j=j+1
            return frase