def uppCons(frase):
    i=0
    frase2=''
    while i<len(frase):
        if frase[i] not in 'bcçdfghjklmnpqrstvwxz':
            frase2+=frase[i]
  
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
        	frase2+=str.upper(frase[i])
    
    	i+=1
    return frase2