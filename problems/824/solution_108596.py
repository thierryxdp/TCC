def uppCons(frase): 
    i=0
    consoantes="BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz"
    while i<len(frase):
        if  frase[i] in consoantes:
            frase=str.replace(frase,frase[i],str.upper)
            frase=nova_frase
            i=i+1
            return frase