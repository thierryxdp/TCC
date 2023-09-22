def posLetra(x,y,z):
	n = 0
	p= 1
    while n<len(x):
        if x[n]==y:
            if p<z:
            	p=p+1
            if p==z:
                return n