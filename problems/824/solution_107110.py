def uppCons(frase):
    x=0
    consoantes=''
    while x<len(frase):
        if frase[x] in 'BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consoantes=str.upper(consoantes)+frase[x]
           
        x=x+1
        return consoantes