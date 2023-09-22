def uppCons(texto):
   	i=0 
    
    while i<len(texto):
        letra=texto[i]
        
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
        
        i = i+1
	
    return texto