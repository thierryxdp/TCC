def par(x):
    return x%2 ==0
def filtra_pares(a):
    p = ()
  		if par(a[0]):
        p = p + (a[0],)
    	elif par(a[1]):
       	p = p + (a[1],)
    	elif par(a[2]):
       	p = p + (a[2],)
    	elif par(a[3]):
        p = p + (a[3],)
    		return p