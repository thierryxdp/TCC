def faltante (L):
  
    n=1
    
    while n<len(L)+1:
    	if n in not L:
        	return n
        else:
            n+=1