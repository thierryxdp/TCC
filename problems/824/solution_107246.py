def uppCons(frase):
    frase=list(frase)
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            letra=str.upper(frase[i])
            consoantes=consoantes+letra
        i=i+1
        consoantes=consoantes+frase[i]
    return consoantes