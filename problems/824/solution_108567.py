def uppCons(frase): 
    i=0
    contador=0
    while i<len(frase):
        frase=str.replace(frase,frase[contador],str.upper)
        nova_frase=frase
        if  frase[i] in "BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz":
             consoante=frase[i]
        i=i+1
    return consoante