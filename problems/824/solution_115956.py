def uppCons(frase):
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç':
            consoantes=consoantes+str.upper(frase[i])
            i=i+1
        elif i<len(frase):
            frase[i] not in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxyzç'
            consoantes=consoantes+frase[i]
            i=i+1
    return consoantes