def uppCons(frase): 
    i=0
    consoante=" "
    while i<len(frase):
        if  frase[i] in "BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz":
             consoante=frase[-1]
        i=i+1
    return consoante