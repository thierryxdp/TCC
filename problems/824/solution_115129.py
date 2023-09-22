def uppCons(f):
    x=''
    i=0
    while i<len(f):
        if f[i] not in 'bcçdfghjklmnpqrstvwxz':
            x+=f[i]
        
  
        if f[i] in 'bcçdfghjklmnpqrstvwxz':
        	x+=f[i].upper()
        	
    
    
    	i+=1
    return x