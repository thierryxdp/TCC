def uppCons(frase):
    consoantes=()
    i=0
    while i<len(frase):
        if frase[i]='bcdfghjklmnpqrstvxwyz':
            consoantes = frase.upper()+frase[i].upper()
        i=i+1
    return consoantes