def uppCons(frase):
    x=0
    consoantes=''
    while x<len(frase):
        if frase[x] in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consoantes=consoantes+frase[x]
           
        x=x+1
    str.upper(consoantes)
    return frase