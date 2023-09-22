def uppCons(frase):
    frase=list(frase)
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            consoantes=consoantes+frase[i]
            frase[i]=str.upper(frase[i])
        i=i+1
    return frase