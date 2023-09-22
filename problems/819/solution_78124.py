def filtraMultiplos(lista,n):
    
    i=0
    r=[]
    while i < len(lista):
        if lista[i] % n == 0:
         	r = r + lista[i]
      		i = i+1
		else:
            i=i+1
        
       	return r