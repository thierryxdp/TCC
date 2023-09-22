def uppCons(f):
    x=''
    i=0
    while i<len(f):
        if f[i] not in 'bcdfghjklmnpqrstvwxz':
            x+=f[i]
        
  
        if f[i] in 'bcdfghjklmnpqrstvwxz':
        	x+=f[1]
        	
    
    
    	i+=1
    return x