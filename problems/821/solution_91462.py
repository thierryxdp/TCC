def fatorial(n):
    i = n
    if n != 1:
    	while i>=2:
        	i=i-1
        	a=n*i
        	n=a
        return a
    else: 
        return 1