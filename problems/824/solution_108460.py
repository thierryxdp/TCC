def uppCons(frase):
    consoantes=1
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return consoantes