def uppCons(frase):
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            letra=str.upper(frase[i])
            consoantes=consoantes+letra
        else:
            consoantes=consoantes+frase[i]
        i=i+1
    return consoantes