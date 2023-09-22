def fatorial(n):
	i=1
    R=1
    if n>0:
    	while i<=n:
        	R=i*R
        	i+=1
        return R
    elif n<0:
    	return 'não existe'
    else:
        return R