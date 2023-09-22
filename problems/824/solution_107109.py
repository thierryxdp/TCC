def uppCons(frase):
    x=0
    consoantes='BCDFGHKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    while x<len(frase):
        if frase[x] in consoantes:
            consoantes=str.upper(consoantes)+frase[x]
           
        x=x+1
    
    return frase+str.upper(consoantes in frase)