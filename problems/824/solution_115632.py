def uppCons(frase):
    i=0
    frase2=''
    while i<len(frase):
        if f[i] not in 'bcçdfghjklmnpqrstvwxz':
            frase2+=frase[i]
  
        if f[i] in 'bcçdfghjklmnpqrstvwxz':
        	frase2+=str.upper(frase[i])
    
    	i+=1
    return frase2