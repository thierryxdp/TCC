def uppCons(frase):
    i=0
    frasemscl=''
    while i<len(frase):
        if frase[i]!='aeiouAEIOU':
            frasemscl=frase.replace(frase[i],str.upper(frase[i]))    
    i=i+1
    return frasemscl