def uppCons(texto,i):
    l=0
    frase=''
    while i<len(texto):
        if f[i] not in 'bcçdfghjklmnpqrstvwxz':
            frase+=texto[l]
  
        if f[l] in 'bcçdfghjklmnpqrstvwxz':
        	frase+=str.upper(texto[l])
    
    	l+=1
    return frase