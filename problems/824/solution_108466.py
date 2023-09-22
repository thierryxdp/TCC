def uppCons(frase):
    consoantes=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            consoantes = frase.replace(frase[i],frase[i].upper())
       
    return consoantes