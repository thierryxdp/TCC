def uppCons(frase):
    consoante='bcdfghjklmnpqrstvxwyz'
    j=0
    while j<len(frase):
        if frase[j] in consoante:
          frase[j].upper()
        j=j+1
    return frase