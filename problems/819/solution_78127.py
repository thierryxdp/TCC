def filtraMultiplos(lista,n):
    
    i=0
    r=[]
    while i < len(lista):
        num = lista[i]
        if num%n==0:
            r = r + lista[i]
      	    i = i+1
	else:
            i=i+1
        
       	return r