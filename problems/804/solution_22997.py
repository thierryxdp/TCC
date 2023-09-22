def par(x):
    return x%2 ==0
def filtra_pares(a,b,c,d):
    p = ()
  	if par(a):
    	p = p + (a,)
    elif par(b):
       	p = p + (b,)
    elif par(c):
       	p = p + (c,)
    elif par(d):
        p = p + (d,)
    		return p