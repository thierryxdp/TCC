def uppCons(frase):
    cons=0
    i=0
    while i<len(frase):
        if frase[i]in 'BCDFGHJKLMNPQRSTVWXYZÇbcdfghjklmnpqrstvwxzç':
            cons= cons+str.upper(frase[i])
        else:
            cons=cons+frase[i]
        i=i+1     
    return cons