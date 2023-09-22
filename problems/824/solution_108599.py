def uppCons(frase): 
    i=0
    consoantes="BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz"
    while i<len(frase):
        frase=str.replace(frase,frase[i],str.upper)
        if  frase[i] in consoantes:
            frase=nova_frase
        i=i+1
    return nova_frase