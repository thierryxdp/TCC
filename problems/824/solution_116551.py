def uppCons(frase):
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'bcdfghijklmnpqrstvwxyz':
             consoantes=consoantes.upper+texto[i]
        i=i+1
    return consoantes