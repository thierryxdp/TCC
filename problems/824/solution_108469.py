def uppCons(frase):
    consoantes=''
    i=0
    while i<len(frase):
        if frase[i+1] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase.replace(frase[i],frase[i].upper())
        i=i+1
    return consoantes