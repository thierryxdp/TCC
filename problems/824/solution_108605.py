def uppCons(frase): 
    i=0
    while i<len(frase):
        if  frase[i]:
            frase=str.replace(frase,frase[i],str.upper("BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz")))
            i=i+1
    return frase