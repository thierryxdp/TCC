def uppCons(frase):
    consoantes=()
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase+frase[i].upper('bcdfghjklmnpqrstvxwyz')
        i=i+1
    return consoantes