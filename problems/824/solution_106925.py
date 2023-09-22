def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz':
            i=i+1
            return str.upper(frase)