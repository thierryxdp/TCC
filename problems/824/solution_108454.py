def uppCons(frase):
    consoantes=frase[]
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return consoantes