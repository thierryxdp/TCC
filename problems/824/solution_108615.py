def uppCons(frase): 
    i=0
    while i<len(frase):
        if  frase[i]:
            frase=str.replace(frase,frase[i],str.upper(frase[0:5]))
            i=i+1
    return frase