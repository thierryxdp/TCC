def uppCons(frase):
    consoantes=()
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase[i].upper()
        i=i-1
    return consoantes