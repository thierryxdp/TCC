def uppCons(texto):
    l=0
    frase=''
    while l<len(texto):
        if texto[l] not in 'bcçdfghjklmnpqrstvwxz':
            frase+=texto[l]    
    	l+=1
    return frase